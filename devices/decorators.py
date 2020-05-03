from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404

from .models import Device


def device_view_permission(old_function):
    def new_function(request, pk, *args, **kwargs):
        device = get_object_or_404(Device, pk=pk)
        user = request.user
        if user.has_perm('customers.view_customer', device.customer):
            return old_function(request, pk)
        else:
            return HttpResponseForbidden(
                "You're not allowed to access this device."
                )
    return new_function
