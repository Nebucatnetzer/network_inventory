from django.db import models

from softwares.models import OperatingSystem
from softwares.models import Software
from softwares.models import SoftwareArchitecture

from .cpu import Cpu
from devices.models import Device
from .disk import Disk
from .gpu import Gpu
from .ram import Ram


class Computer(Device):
    os = models.ForeignKey(OperatingSystem, models.SET_NULL, blank=True,
                           null=True, verbose_name='OS')
    cpu = models.ManyToManyField(Cpu, through='ComputerCpuRelation')
    ram = models.ManyToManyField(Ram, through='ComputerRamRelation')
    gpu = models.ManyToManyField(Gpu, through='ComputerGpuRelation')
    disks = models.ManyToManyField(Disk, through='ComputerDiskRelation')
    software = models.ManyToManyField(Software,
                                      through='ComputerSoftwareRelation')
    host = models.ForeignKey('self', null=True, blank=True,
                             on_delete=models.CASCADE)
    allocated_space = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('computer', args=[str(self.id)])


class ComputerCpuRelation(models.Model):
    cpu = models.ForeignKey(Cpu, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return str(self.computer)

    class Meta:
        verbose_name_plural = "CPUs in Computer"


class ComputerRamRelation(models.Model):
    ram = models.ForeignKey(Ram, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return str(self.computer)

    class Meta:
        verbose_name_plural = "RAM Modules in Computer"


class ComputerDiskRelation(models.Model):
    disk = models.ForeignKey(Disk, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return str(self.computer)

    class Meta:
        verbose_name_plural = "Disks in Computer"


class ComputerSoftwareRelation(models.Model):
    software = models.ForeignKey(Software, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    architecture = models.ForeignKey(SoftwareArchitecture, models.SET_NULL,
                                     blank=True, null=True)

    def __str__(self):
        return str(self.computer)

    class Meta:
        verbose_name_plural = "Software on Computer"


class ComputerGpuRelation(models.Model):
    gpu = models.ForeignKey(Gpu, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return str(self.computer)

    class Meta:
        verbose_name_plural = "GPUs in Computer"
