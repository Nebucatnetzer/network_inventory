from django.contrib.admin.views.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME


def superuser_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME,
                       login_url='account_login_url'):
    """
    Decorator for views that checks that the user is logged in and is a
    superuser, redirecting to the login page if necessary.
    https://stackoverflow.com/a/46318226/7723859
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator
