from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from guardian.shortcuts import get_objects_for_user
from .models import (GeneralDevice, Computer, CronJob,
                     ComputerRamRelation,
                     ComputerDiskRelation,
                     ComputerCpuRelation)


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


class ComputerList(ListView):
    model = Computer
    template_name = 'inventory/computer_list.html'

    def get_queryset(self):
        queryset = get_objects_for_user(self.request.user, 'inventory.view_computer', klass=Computer)
        #return super().get_queryset()
        return queryset



class CronJobList(ListView):
    model = CronJob
    template_name = 'inventory/cronjob_list.html'


class DeviceList(ListView):
    model = GeneralDevice
    context_object_name = 'device_list'
    template_name = 'inventory/device_list.html'
