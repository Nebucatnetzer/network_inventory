from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from django_filters.views import FilterView
from django_tables2 import RequestConfig
from django_tables2.views import SingleTableMixin
from guardian.shortcuts import get_objects_for_user

from backups.models import Backup
from customers.models import Customer
from customers.decorators import customer_view_permission
from devices.models import Warranty
from licenses.models import LicenseWithComputer

from .decorators import computer_view_permission
from .filters import ComputerFilter
from .forms import ComputerCreateForm
from .forms import ComputerUpdateForm
from .models import Computer
from .models import ComputerCpuRelation
from .models import ComputerDiskRelation
from .models import ComputerRamRelation
from .models import ComputerSoftwareRelation
from .models import DisksInRaid
from .models import Raid
from .tables import ComputersTable


@login_required
@computer_view_permission
def computer_detail_view(request, pk):
    device = get_object_or_404(Computer, pk=pk)
    disks_relations = ComputerDiskRelation.objects.filter(computer=pk)
    warranty_relations = Warranty.objects.filter(device=pk)
    ram_relations = ComputerRamRelation.objects.filter(computer=pk)
    cpu_relations = ComputerCpuRelation.objects.filter(computer=pk)
    software_relations = ComputerSoftwareRelation.objects.filter(computer=pk)
    license_list = LicenseWithComputer.objects.filter(computer=pk)
    raid_disk_pairs = {}
    for raid in Raid.objects.filter(computer=pk):
        raid_disk_pairs[raid] = DisksInRaid.objects.filter(raid=raid)
    backup_list = Backup.objects.filter(computer=pk)
    context = {'device': device,
               'warranty_relations': warranty_relations,
               'disks_relations': disks_relations,
               'ram_relations': ram_relations,
               'cpu_relations': cpu_relations,
               'software_relations': software_relations,
               'raid_disk_pairs': raid_disk_pairs,
               'backup_relations': backup_list,
               'license_list': license_list}
    return render(request, 'computers/computer_details.html', context)


@login_required
@customer_view_permission
def computers_table_view(request, pk):
    table = ComputersTable(Computer.objects.filter(customer=pk))
    RequestConfig(request).configure(table)
    return render(request, 'computers/computer_list.html', {'computers': table,
                                                            'pk': pk,})


class ComputersFilterView(LoginRequiredMixin, SingleTableMixin, FilterView):
    table_class = ComputersTable
    model = Computer
    template_name = "computers/all_computers.html"

    filterset_class = ComputerFilter

    def get_queryset(self):
        customers = get_objects_for_user(self.request.user,
                                         'customers.view_customer',
                                         klass=Customer)
        results = Computer.objects.filter(customer__in=customers)
        return results


class ComputerCreateFromCustomerView(LoginRequiredMixin, CreateView):
    form_class = ComputerCreateForm
    template_name = 'computers/computer_create.html'

    def get_success_url(self):
        return reverse('computer_update', args=(self.object.pk,))

    def get_form_kwargs(self):
        """
        Pass the URL variables and the request user to the form.
        """
        kwargs = super(ComputerCreateFromCustomerView, self).get_form_kwargs()
        kwargs.update(self.kwargs)
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_initial(self):
        """
        Set the customer dropdown to the customer from the previews view.
        """
        customer = get_object_or_404(Customer, id=self.kwargs.get('pk'))
        return {
            'customer': customer,
        }


class ComputerUpdateView(LoginRequiredMixin, UpdateView):
    model = Computer
    form_class = ComputerUpdateForm
    template_name = 'computers/computer_update.html'