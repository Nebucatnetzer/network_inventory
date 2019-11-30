from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from .models import Computer, Customer, Device, ConnectedDevice


def computer_view_permission(old_fuction):
    def new_function(request, pk, *args, **kwargs):
        computer = get_object_or_404(Computer, pk=pk)
        customer = Customer.objects.get(pk=computer.customer.pk)
        user = request.user
        if user.has_perm('inventory.view_customer', customer):
            return old_fuction(request, pk)
        else:
            return HttpResponseForbidden(
                "You're not allowed to access this device."
                )
    return new_function


def device_view_permission(old_function):
    def new_function(request, pk, *args, **kwargs):
        device = get_object_or_404(Device, pk=pk)
        customer = Customer.objects.get(pk=device.customer.pk)
        user = request.user
        if user.has_perm('inventory.view_customer', customer):
            return old_function(request, pk)
        else:
            return HttpResponseForbidden(
                "You're not allowed to access this device."
                )
    return new_function


def connect_device_view_permission(old_function):
    def new_function(request, pk, *args, **kwargs):
        device = get_object_or_404(ConnectedDevice, pk=pk)
        customer = Customer.objects.get(pk=device.customer.pk)
        user = request.user
        if user.has_perm('inventory.view_customer', customer):
            return old_fuction(request, pk)
        else:
            return HttpResponseForbidden(
                "You're not allowed to access this device."
                )
    return new_function


def customer_view_permission(old_function):
    def new_function(request, pk, *args, **kwargs):
        customer = Customer.objects.get(pk=pk)
        user = request.user
        if user.has_perm('inventory.view_customer', customer):
            return old_function(request, pk)
        else:
            return HttpResponseForbidden(
                "You're not allowed to access this page."
                )
    return new_function
