from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from guardian.shortcuts import get_objects_for_user
from .decorators import computer_view_permission
from .models import (Device, Computer, ComputerRamRelation,
                     ComputerDiskRelation, ComputerCpuRelation,
                     Customer)


def device_details(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    return render(request, 'inventory/device_details.html',
                  {'device': device})


@login_required
@computer_view_permission
def computer_details(request, computer_id):
    computer = get_object_or_404(Computer, pk=computer_id)
    disks_list = ComputerDiskRelation.objects.filter(computer=computer_id)
    ram_list = ComputerRamRelation.objects.filter(computer=computer_id)
    cpu_list = ComputerCpuRelation.objects.filter(computer=computer_id)
    return render(request, 'inventory/computer_details.html',
                  {'computer': computer,
                   'disks_list': disks_list,
                   'ram_list': ram_list,
                   'cpu_list': cpu_list})


def list_of_lists(request, customer_id):
    return render(request, 'inventory/list_of_lists.html',
                  {'customer_id': customer_id})


class CustomerList(ListView):
    model = Customer
    template_name = 'inventory/customer_list.html'

    def get_queryset(self):
        queryset = get_objects_for_user(self.request.user,
                                        'inventory.view_customer',
                                        klass=Customer)
        return queryset


class ComputerList(ListView):
    model = Computer
    template_name = 'inventory/computer_list.html'

    def get_queryset(self):
        queryset = Computer.objects.filter(customer=self.kwargs['customer_id'])
        return queryset


class DeviceList(ListView):
    model = Device
    context_object_name = 'device_list'
    template_name = 'inventory/device_list.html'

    def get_queryset(self):
        queryset = Device.objects.filter(customer=self.kwargs['customer_id'])
        return queryset

