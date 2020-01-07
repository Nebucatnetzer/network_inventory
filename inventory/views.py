from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from django_filters.views import FilterView
from django_tables2 import RequestConfig
from django_tables2.views import SingleTableMixin
from guardian.shortcuts import get_objects_for_user

from customer.models import Customer
from customer.decorators import customer_view_permission

from .decorators import backup_view_permission
from .decorators import computer_view_permission
from .decorators import device_view_permission
from .decorators import net_view_permission
from .decorators import user_view_permission
from .filters import ComputerFilter
from .models import Backup
from .models import Computer
from .models import ComputerCpuRelation
from .models import ComputerDiskRelation
from .models import ComputerLicense
from .models import ComputerRamRelation
from .models import ComputerSoftwareRelation
from .models import Device
from .models import DeviceInNet
from .models import DisksInRaid
from .models import LicenseWithComputer
from .models import LicenseWithUser
from .models import MailAlias
from .models import Net
from .models import NotificationFromBackup
from .models import Raid
from .models import TargetDevice
from .models import User
from .models import UserInAdGroup
from .models import UserInMailGroup
from .models import UserLicense
from .tables import BackupsTable
from .tables import ComputerLicensesTable
from .tables import ComputersTable
from .tables import DevicesTable
from .tables import NetDetailTable
from .tables import NetsTable
from .tables import UserLicensesTable
from .tables import UsersTable


@login_required
@device_view_permission
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
    licenses = LicenseWithComputer.objects.filter(computer=pk)
    raid_disk_pairs = {}
    for raid in Raid.objects.filter(computer=pk):
        raid_disk_pairs[raid] = DisksInRaid.objects.filter(raid=raid)
    backup_list = Backup.objects.filter(computer=pk)
    context = {'computer': computer,
               'disks_list': disks_list,
               'ram_list': ram_list,
               'cpu_list': cpu_list,
               'software_list': software_list,
               'raid_disk_pairs': raid_disk_pairs,
               'backup_list': backup_list,
               'licenses': licenses}
    return render(request, 'inventory/computer_details.html', context)


@login_required
@customer_view_permission
def computers_table_view(request, pk):
    table = ComputersTable(Computer.objects.filter(customer=pk))
    RequestConfig(request).configure(table)
    return render(request, 'inventory/computer_list.html', {'computers': table})


@login_required
@customer_view_permission
def devices_table_view(request, pk):
    table = DevicesTable(Device.objects.filter(customer=pk))
    RequestConfig(request).configure(table)
    return render(request, 'inventory/device_list.html', {'devices': table})


@login_required
@customer_view_permission
def nets_table_view(request, pk):
    table = NetsTable(Net.objects.filter(customer=pk))
    RequestConfig(request).configure(table)
    return render(request, 'inventory/net_list.html', {'nets': table})


@login_required
@net_view_permission
def net_detail_view(request, pk):
    net = get_object_or_404(Net, pk=pk)
    table = NetDetailTable(DeviceInNet.objects.filter(net=net))
    RequestConfig(request).configure(table)
    return render(request, 'inventory/net_details.html',
                  {'table': table,
                   'net': net})


@login_required
@customer_view_permission
def backups_table_view(request, pk):
    computers = Computer.objects.filter(customer=pk)
    table = BackupsTable(Backup.objects.filter(computer__in=computers))
    RequestConfig(request).configure(table)
    return render(request, 'inventory/backup_list.html', {'backups': table})


@login_required
@backup_view_permission
def backup_detail_view(request, pk):
    backup = get_object_or_404(Backup, pk=pk)
    target_device_list = TargetDevice.objects.filter(backup=backup)
    notifications = NotificationFromBackup.objects.filter(backup=backup)
    return render(request, 'inventory/backup_details.html',
                  {'backup': backup,
                   'target_device_list': target_device_list,
                   'notifications': notifications})


class ComputersFilterView(LoginRequiredMixin, SingleTableMixin, FilterView):
    table_class = ComputersTable
    model = Computer
    template_name = "inventory/all_computers.html"

    filterset_class = ComputerFilter

    def get_queryset(self):
        customers = get_objects_for_user(self.request.user,
                                         'customer.view_customer',
                                         klass=Customer)
        results = Computer.objects.filter(customer__in=customers)
        return results


@login_required
@customer_view_permission
def licenses_table_view(request, pk):
    user_licenses = UserLicensesTable(UserLicense.objects.filter(customer=pk))
    computer_licenses = ComputerLicensesTable(
        ComputerLicense.objects.filter(customer=pk))
    RequestConfig(request).configure(user_licenses)
    RequestConfig(request).configure(computer_licenses)
    return render(request,
                  'inventory/license_list.html',
                  {'user_licenses': user_licenses,
                   'computer_licenses': computer_licenses})


@login_required
@customer_view_permission
def users_table_view(request, pk):
    table = UsersTable(User.objects.filter(customer=pk))
    RequestConfig(request).configure(table)
    return render(request, 'inventory/user_list.html', {'users': table})


@login_required
@user_view_permission
def user_detail_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    ad_groups = UserInAdGroup.objects.filter(user=user)
    mail_groups = UserInMailGroup.objects.filter(user=user)
    mail_alias = MailAlias.objects.filter(user=user)
    computers = Computer.objects.filter(user=user)
    licenses = LicenseWithUser.objects.filter(user=user)
    return render(request, 'inventory/user_details.html',
                  {'user': user,
                   'ad_groups': ad_groups,
                   'mail_groups': mail_groups,
                   'mail_alias': mail_alias,
                   'computers': computers,
                   'licenses': licenses})
