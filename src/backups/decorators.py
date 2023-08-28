from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404

from .models import Backup


def backup_view_permission(old_fuction):
    def new_function(request, pk, *args, **kwargs):
        backup = get_object_or_404(Backup, pk=pk)
        user = request.user
        if user.has_perm("customers.view_customer", backup.computer.customer):
            return old_fuction(request, pk)
        else:
            return HttpResponseForbidden("You're not allowed to access this device.")

    return new_function
