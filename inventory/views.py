#!/usr/bin/python3
from django.shortcuts import get_object_or_404, render
from .models import (Device, Computer, CronJob,
                     ComputerRamRelation,
                     ComputerDiskRelation,
                     ComputerCpuRelation)


def index(request):
    device_list = Device.objects.all()
    computer_list = Computer.objects.all()

    return render(request,
                  'inventory/index.html',
                  {'device_list': device_list,
                   'computer_list': computer_list})


def device_details(request, device_id):
        device = get_object_or_404(Device, pk=device_id)
        return render(request, 'inventory/device_details.html',
                      {'device': device})


