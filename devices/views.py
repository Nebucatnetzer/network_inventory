from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from django_tables2 import RequestConfig

from customers.decorators import customer_view_permission

from .decorators import device_view_permission

from .models import Device
from .tables import DevicesTable


@login_required
@device_view_permission
def device_detail_view(request, pk):
    device = get_object_or_404(Device, pk=pk)
    return render(request, 'inventory/device_details.html',
                  {'device': device})


@login_required
@customer_view_permission
def devices_table_view(request, pk):
    table = DevicesTable(Device.objects.filter(customer=pk))
    RequestConfig(request).configure(table)
    return render(request, 'inventory/device_list.html', {'devices': table})
