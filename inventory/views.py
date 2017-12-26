#!/usr/bin/python3
from django.shortcuts import get_object_or_404, render
from .models import (GeneralDevice, Computer, CronJob,
                     ComputerRamRelation,
                     ComputerDiskRelation,
                     ComputerCpuRelation)


def index(request):
    device_list = GeneralDevice.objects.all()
    computer_list = Computer.objects.all().order_by('ip')
    cronjob_list = CronJob.objects.all().order_by('host')

    return render(request,
                  'inventory/index.html',
                  {'device_list': device_list,
                   'computer_list': computer_list,
                   'cronjob_list': cronjob_list})


def device_details(request, device_id):
        device = get_object_or_404(GeneralDevice, pk=device_id)
        return render(request, 'inventory/device_details.html',
                      {'device': device})


def computer_details(request, computer_id):
        computer = get_object_or_404(Computer, pk=computer_id)
        disks_list = ComputerDiskRelation.objects.filter(computer=computer_id)
        ram = ComputerRamRelation.objects.get(computer=computer_id)
        cpu = ComputerCpuRelation.objects.get(computer=computer_id)
        cronjob_list = CronJob.objects.filter(host=computer_id)
        return render(request, 'inventory/computer_details.html',
                      {'computer': computer,
                       'disks_list': disks_list,
                       'ram': ram,
                       'cpu': cpu,
                       'cronjob_list': cronjob_list})


def cronjob_details(request, cronjob_id):
        cronjob = get_object_or_404(CronJob, pk=cronjob_id)
        return render(request, 'inventory/cronjob_details.html',
                      {'cronjob': cronjob})
