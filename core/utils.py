from django.apps import apps
from django.http import Http404
from django.shortcuts import get_object_or_404
from guardian.shortcuts import get_objects_for_user

from customers.models import Customer


def td_format(td_object):
    """A helper function to convert time deltas to a human readable format.
       Taken from here."""
    seconds = int(td_object.total_seconds())
    periods = [
        ('year',        60*60*24*365),
        ('month',       60*60*24*30),
        ('day',         60*60*24),
        ('hour',        60*60),
        ('minute',      60),
        ('second',      1)
    ]

    strings = []
    for period_name, period_seconds in periods:
        if seconds >= period_seconds:
            period_value, seconds = divmod(seconds, period_seconds)
            has_s = 's' if period_value > 1 else ''
            strings.append("%s %s%s" % (period_value, period_name, has_s))

    return ", ".join(strings)


def get_customers(user):
    """
    Returns a queryset of customers the user is allowed to view.

    user : django.contrib.auth.models.User
    """
    return get_objects_for_user(user,
                                'customers.view_customer',
                                klass=Customer)


def get_objects(model_name, user):
    """
    Returns a queryset of a given model name the user is allowed to view.

    model_name: string
    user : django.contrib.auth.models.User
    """
    model_name = model_name.lower()
    customers = get_customers(user)
    app_names = [
        'backups',
        'computers',
        'core',
        'customers',
        'devices',
        'licenses',
        'nets',
        'softwares',
        'users',
    ]
    for name in app_names:
        app = apps.get_app_config(name)
        if model_name in app.models:
            model = app.models[model_name]
            return model.objects.filter(customer__in=customers)
    raise Http404("Model ", model_name, " not found.")


def get_object_with_view_permission(model, user=None, pk=None):
    requested_object = get_object_or_404(model, id=pk)
    permission = "customers.view_customer"
    if model.__name__ == 'Customer':
        customer = requested_object
    else:
        customer = get_object_or_404(
            Customer, name=requested_object.customer)
    if user.has_perm(permission, customer):
        return requested_object
    raise Http404()


def get_objects_with_view_permission(model, user=None):
    customers = get_customers(user)
    if model.__name__ == 'Customer':
        return customers
    objects = model.objects.filter(customer__in=customers)
    if not objects:
        raise Http404()
    return objects
