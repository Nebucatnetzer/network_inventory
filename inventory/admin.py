#!/usr/bin/python3
from django.contrib import admin
from inventory.models import (Device, Weekday, Month, RamType, Ram,
                              DiskType, DiskSize, Disk, Architecture,
                              CpuManufacturer, Cpu, OperatingSystem, Raid,
                              Computer, ComputerDiskRelation,
                              ComputerRamRelation, Warranty, CronJob)


class RamInline(admin.StackedInline):
    model = ComputerRamRelation
    verbose_name_plural = 'Ram Modules'


class DiskInline(admin.StackedInline):
    model = ComputerDiskRelation
    verbose_name_plural = 'Disks'


class ComputerAdmin(admin.ModelAdmin):
    inlines = (RamInline, DiskInline)


admin.site.register(Device)
admin.site.register(Weekday)
admin.site.register(Month)
admin.site.register(RamType)
admin.site.register(Ram)
admin.site.register(DiskType)
admin.site.register(DiskSize)
admin.site.register(Disk)
admin.site.register(Architecture)
admin.site.register(CpuManufacturer)
admin.site.register(Cpu)
admin.site.register(OperatingSystem)
admin.site.register(Raid)
admin.site.register(Computer)
admin.site.register(ComputerDiskRelation)
admin.site.register(ComputerRamRelation)
admin.site.register(Warranty)
admin.site.register(CronJob)
