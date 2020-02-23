from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from django_tables2 import RequestConfig

from core.decorators import superuser_required
from customers.decorators import customer_view_permission

from .decorators import device_view_permission
from .decorators import connected_device_view_permission

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
    return render(request, 'devices/device_details.html',
                  {'device': device,
                   'warranty_relations': warranty_relations})


@login_required
@customer_view_permission
def devices_table_view(request, pk):
    table = DevicesTable(Device.objects.filter(customer=pk))
    RequestConfig(request).configure(table)
    return render(request, 'devices/device_list.html', {'devices': table})


@login_required
@connected_device_view_permission
def connected_device_detail_view(request, pk):
    device = get_object_or_404(ConnectedDevice, pk=pk)
    warranty_relations = Warranty.objects.filter(device=pk)
    return render(request, 'devices/device_details.html',
                  {'device': device,
                   'warranty_relations': warranty_relations})


@login_required
@customer_view_permission
def connected_devices_table_view(request, pk):
    table = ConnectedDevicesTable(ConnectedDevice.objects.filter(customer=pk))
    RequestConfig(request).configure(table)
    return render(request, 'devices/connected_device_list.html', {'devices': table})


@login_required
@superuser_required
def warranties_view(request):
    table = WarrantiesTable(Warranty.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'devices/warranties_list.html', {'devices': table})
