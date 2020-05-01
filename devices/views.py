from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import UpdateView

from django_tables2 import RequestConfig

from customers.decorators import customer_view_permission
from customers.models import Customer
from core.utils import get_objects

from .decorators import device_view_permission
from .decorators import connected_device_view_permission

from .forms import DeviceCreateForm
from .forms import DeviceUpdateForm
from .forms import WarrantyCreateForm

from .models import ConnectedDevice
from .models import Device
from .models import Warranty

from .tables import ConnectedDevicesTable
from .tables import DevicesTable
from .tables import WarrantiesTable


@login_required
@device_view_permission
def device_detail_view(request, pk):
    device = get_object_or_404(Device, pk=pk)
    warranty_relations = Warranty.objects.filter(device=pk)
    return render(request,
                  'devices/device_details.html',
                  {'device': device,
                   'warranty_relations': warranty_relations,
                   'pk': pk})


@login_required
@customer_view_permission
def devices_table_view(request, pk):
    table = DevicesTable(Device.objects.filter(customer=pk))
    RequestConfig(request).configure(table)
    return render(request,
                  'devices/device_list.html',
                  {'devices': table,
                   'pk': pk})


@login_required
@connected_device_view_permission
def connected_device_detail_view(request, pk):
    device = get_object_or_404(ConnectedDevice, pk=pk)
    warranty_relations = Warranty.objects.filter(device=pk)
    return render(request,
                  'devices/device_details.html',
                  {'device': device,
                   'warranty_relations': warranty_relations,
                   'pk': pk})


@login_required
@customer_view_permission
def connected_devices_table_view(request, pk):
    table = ConnectedDevicesTable(ConnectedDevice.objects.filter(customer=pk))
    RequestConfig(request).configure(table)
    return render(request,
                  'devices/connected_device_list.html',
                  {'devices': table})


@login_required
def warranties_view(request):
    table = WarrantiesTable(get_objects("Warranty", request.user))
    RequestConfig(request).configure(table)
    return render(request,
                  'devices/warranties_list.html',
                  {'devices': table})


class DeviceCreateFromCustomerView(LoginRequiredMixin, CreateView):
    """
    A view to show a DeviceCreateForm after comming from a customers device
    table. The customer will be preselected in the form.
    """
    form_class = DeviceCreateForm
    template_name = 'devices/device_create.html'

    def get_success_url(self):
        return reverse('device_update', args=(self.object.pk,))

    def get_form_kwargs(self):
        """
        Pass the request user to the form.
        """
        kwargs = super(DeviceCreateFromCustomerView, self).get_form_kwargs()
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


class DeviceUpdateView(LoginRequiredMixin, UpdateView):
    model = Device
    form_class = DeviceUpdateForm
    template_name = 'devices/device_update.html'


class WarrantyCreateView(LoginRequiredMixin, CreateView):
    model = Warranty
    form_class = WarrantyCreateForm
    template_name = 'devices/warranty_create.html'

    def get_success_url(self):
        return reverse('device', args=(self.kwargs.get('pk'),))

    def get_initial(self):
        """
        Set the device and customer dropdown to the device from the previous
        view and the customer related to the device.
        """
        self.device = get_object_or_404(Device, id=self.kwargs.get('pk'))
        return {
            'device': self.device,
            'customer': self.device.customer,
        }
