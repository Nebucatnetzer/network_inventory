from django.contrib import admin
from inventory.models import (Device, Weekday, Month, RamType, Ram,
                              DiskType, DiskSize, Disk, Architecture,
                              CpuManufacturer, Cpu, OperatingSystem,
                              Raid, Computer, ComputerDiskRelation,
                              ComputerCpuRelation,
                              ComputerRamRelation, Warranty, CronJob)


class RamInLine(admin.StackedInline):
    model = ComputerRamRelation
    extra = 0
    verbose_name_plural = 'RAM Modules'


class DiskInLine(admin.StackedInline):
    model = ComputerDiskRelation
    extra = 0
    verbose_name_plural = 'Disks'


class CpusInLine(admin.StackedInline):
    model = ComputerCpuRelation
    extra = 0
    verbose_name_plural = 'CPUs'


class ComputerAdmin(admin.ModelAdmin):
    inlines = (CpusInLine, RamInLine, DiskInLine,)


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
