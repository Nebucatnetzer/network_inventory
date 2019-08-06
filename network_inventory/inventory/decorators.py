from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from .models import Computer, Customer, Device, ConnectedDevice


def computer_view_permission(old_fuction):
    def new_function(request, computer_id, *args, **kwargs):
        computer = get_object_or_404(Computer, pk=computer_id)
        customer = Customer.objects.get(pk=computer.customer.pk)
        user = request.user
        if user.has_perm('inventory.view_customer', customer):
            return old_fuction(request, computer_id)
        else:
            return HttpResponseForbidden(
                "You're not allowed to access this device."
                )
    return new_function


def device_view_permission(old_function):
    def new_function(request, device_id, *args, **kwargs):
        device = get_object_or_404(Device, pk=device_id)
        customer = Customer.objects.get(pk=device.customer.pk)
        user = request.user
        if user.has_perm('inventory.view_customer', customer):
            return old_fuction(request, device_id)
        else:
            return HttpResponseForbidden(
                "You're not allowed to access this device."
                )
    return new_function


def connect_device_view_permission(old_function):
    def new_function(request, device_id, *args, **kwargs):
        device = get_object_or_404(ConnectedDevice, pk=device_id)
        customer = Customer.objects.get(pk=device.customer.pk)
        user = request.user
        if user.has_perm('inventory.view_customer', customer):
            return old_fuction(request, device_id)
        else:
            return HttpResponseForbidden(
                "You're not allowed to access this device."
                )
    return new_function
