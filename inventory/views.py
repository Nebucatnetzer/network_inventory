from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from django_filters.views import FilterView
from django_tables2 import RequestConfig
from django_tables2.views import SingleTableMixin
from guardian.shortcuts import get_objects_for_user

from backups.models import Backup
from customers.models import Customer
from customers.decorators import customer_view_permission

from .decorators import computer_view_permission
from .filters import ComputerFilter
from .models import Computer
from .models import ComputerCpuRelation
from .models import ComputerDiskRelation
from .models import ComputerLicense
from .models import ComputerRamRelation
from .models import ComputerSoftwareRelation
from .models import DisksInRaid
from .models import LicenseWithComputer
from .models import Raid
from .models import UserLicense
from .tables import ComputerLicensesTable
from .tables import ComputersTable
from .tables import UserLicensesTable


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


class ComputersFilterView(LoginRequiredMixin, SingleTableMixin, FilterView):
    table_class = ComputersTable
    model = Computer
    template_name = "inventory/all_computers.html"

    filterset_class = ComputerFilter

    def get_queryset(self):
        customers = get_objects_for_user(self.request.user,
                                         'customers.view_customer',
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
