from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from .models import Backup
from .models import Computer
from .models import Customer
from .models import Device
from .models import ConnectedDevice
from .models import Net
from .models import User


def computer_view_permission(old_fuction):
    def new_function(request, pk, *args, **kwargs):
        computer = get_object_or_404(Computer, pk=pk)
        user = request.user
        if user.has_perm('inventory.view_customer', computer.customer):
            return old_fuction(request, pk)
        else:
            return HttpResponseForbidden(
                "You're not allowed to access this device."
                )
    return new_function


def device_view_permission(old_function):
    def new_function(request, pk, *args, **kwargs):
        device = get_object_or_404(Device, pk=pk)
        user = request.user
        if user.has_perm('inventory.view_customer', device.customer):
            return old_function(request, pk)
        else:
            return HttpResponseForbidden(
                "You're not allowed to access this device."
                )
    return new_function


def connect_device_view_permission(old_function):
    def new_function(request, pk, *args, **kwargs):
        device = get_object_or_404(ConnectedDevice, pk=pk)
        user = request.user
        if user.has_perm('inventory.view_customer', device.customer):
            return old_function(request, pk)
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


def net_view_permission(old_fuction):
    def new_function(request, pk, *args, **kwargs):
        net = get_object_or_404(Net, pk=pk)
        user = request.user
        if user.has_perm('inventory.view_customer', net.customer):
            return old_fuction(request, pk)
        else:
            return HttpResponseForbidden(
                "You're not allowed to access this device."
                )
    return new_function


def backup_view_permission(old_fuction):
    def new_function(request, pk, *args, **kwargs):
        backup = get_object_or_404(Backup, pk=pk)
        user = request.user
        if user.has_perm('inventory.view_customer', backup.computer.customer):
            return old_fuction(request, pk)
        else:
            return HttpResponseForbidden(
                "You're not allowed to access this device."
                )
    return new_function


def user_view_permission(old_fuction):
    def new_function(request, pk, *args, **kwargs):
        inventory_user = get_object_or_404(User, pk=pk)
        user = request.user
        if user.has_perm('inventory.view_customer', inventory_user.customer):
            return old_fuction(request, pk)
        else:
            return HttpResponseForbidden(
                "You're not allowed to access this device."
                )
    return new_function
