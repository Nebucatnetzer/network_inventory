from django.http import HttpResponseForbidden
from inventory.models import Computer, Customer


def computer_view_permission(old_fuction):
    def new_function(request, computer_id, *args, **kwargs):
        computer = Computer.objects.get(pk=computer_id)
        customer = Customer.objects.get(pk=computer.customer.pk)
        user = request.user
        if user.has_perm('inventory.view_customer', customer):
            return old_fuction(request, computer_id)
        else:
            return HttpResponseForbidden(
                "You're not allowed to access this device."
                )
    return new_function