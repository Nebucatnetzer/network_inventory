from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404

from .models import Computer


def computer_view_permission(old_fuction):
    def new_function(request, pk, *args, **kwargs):
        computer = get_object_or_404(Computer, pk=pk)
        user = request.user
        if user.has_perm('customers.view_customer', computer.customer):
            return old_fuction(request, pk)
        else:
            return HttpResponseForbidden(
                "You're not allowed to access this device."
                )
    return new_function
