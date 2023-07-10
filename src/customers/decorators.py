from django.http import HttpResponseForbidden

from .models import Customer


def customer_view_permission(old_function):
    def new_function(request, pk, *args, **kwargs):
        customer = Customer.objects.get(pk=pk)
        user = request.user
        if user.has_perm("customers.view_customer", customer):
            return old_function(request, pk)
        else:
            return HttpResponseForbidden("You're not allowed to access this page.")

    return new_function
