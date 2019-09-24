from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView

from guardian.shortcuts import get_objects_for_user
from guardian.mixins import PermissionRequiredMixin

from django_tables2 import RequestConfig
from django_tables2.views import SingleTableMixin

from django_filters.views import FilterView

from .decorators import computer_view_permission
from .models import (Device, Computer, ComputerRamRelation,
                     ComputerDiskRelation, ComputerCpuRelation,
                     ComputerSoftwareRelation, Customer, Net, RaidInComputer,
                     Backup, DeviceInNet)
from .tables import (CustomersTable, ComputersTable, DevicesTable, NetsTable,
                     BackupsTable, NetDetailTable, BackupDetailTable)
from .filters import ComputerFilter


@login_required
def device_detail_view(request, pk):
    device = get_object_or_404(Device, pk=pk)
    return render(request, 'inventory/device_details.html',
                  {'device': device})


@login_required
@computer_view_permission
def computer_detail_view(request, pk):
    computer = get_object_or_404(Computer, pk=pk)
    disks_list = ComputerDiskRelation.objects.filter(computer=pk)
    ram_list = ComputerRamRelation.objects.filter(computer=pk)
    cpu_list = ComputerCpuRelation.objects.filter(computer=pk)
    software_list = ComputerSoftwareRelation.objects.filter(computer=pk)
    raid_relations = RaidInComputer.objects.filter(computer=pk)
    raid_relations = RaidInComputer.objects.filter(computer=pk)
    backup_list = Backup.objects.filter(computer=pk)
    context = {'computer': computer,
               'disks_list': disks_list,
               'ram_list': ram_list,
               'cpu_list': cpu_list,
               'software_list': software_list,
               'raid_relations': raid_relations,
               'backup_list': backup_list }
    return render(request, 'inventory/computer_details.html', context)


class CustomerDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Customer
    template_name = 'inventory/customer_details.html'
    permission_required = 'view_customer'


@login_required
def customers_table_view(request):
    table = CustomersTable(
        get_objects_for_user(request.user,
                             'inventory.view_customer',
                             klass=Customer))
    RequestConfig(request).configure(table)
    return render(request, 'inventory/customer_list.html', {'customers': table})


@login_required
def computers_table_view(request, pk):
    table = ComputersTable(Computer.objects.filter(customer=pk))
    RequestConfig(request).configure(table)
    return render(request, 'inventory/computer_list.html', {'computers': table})


@login_required
def devices_table_view(request, pk):
    table = DevicesTable(Device.objects.filter(customer=pk))
    RequestConfig(request).configure(table)
    return render(request, 'inventory/device_list.html', {'devices': table})


@login_required
def nets_table_view(request, pk):
    table = NetsTable(Net.objects.filter(customer=pk))
    RequestConfig(request).configure(table)
    return render(request, 'inventory/net_list.html', {'nets': table})


@login_required
def net_detail_view(request, pk):
    net = get_object_or_404(Net, pk=pk)
    table = NetDetailTable(DeviceInNet.objects.filter(net=net))
    RequestConfig(request).configure(table)
    return render(request, 'inventory/net_details.html',
                  {'table': table,
                   'net': net})


@login_required
def backups_table_view(request, pk):
    computers = Computer.objects.filter(customer=pk)
    table = BackupsTable(Backup.objects.filter(computer__in=computers))
    RequestConfig(request).configure(table)
    return render(request, 'inventory/backup_list.html', {'backups': table})


@login_required
def backup_detail_view(request, pk):
    table = BackupDetailTable(Backup.objects.filter(pk=pk))
    RequestConfig(request).configure(table)
    return render(request, 'inventory/backup_details.html', {'backup': table})


class ComputersFilterView(LoginRequiredMixin, SingleTableMixin, FilterView):
    table_class = ComputersTable
    model = Computer
    template_name = "inventory/all_computers.html"

    filterset_class = ComputerFilter

    def get_queryset(self):
        customers = get_objects_for_user(self.request.user, 'inventory.view_customer', klass=Customer)
        results = Computer.objects.filter(customer__in=customers)
        return results
