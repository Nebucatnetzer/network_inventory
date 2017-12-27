from django.contrib import admin
from inventory.models import (GeneralDevice, HoursInDay,
                              MinutesInHour, Weekday, DayOfMonth,
                              Month, RamType, Ram, DiskType, DiskSize,
                              Disk, Architecture, CpuManufacturer,
                              Cpu, OperatingSystem, Raid, Computer,
                              ComputerDiskRelation,
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
    list_display = ('name', 'ip', 'host')
    inlines = (CpusInLine, RamInLine, DiskInLine,)


class CronJobAdmin(admin.ModelAdmin):
    list_display = ('name', 'host')


admin.site.register(GeneralDevice)
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
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Warranty)
admin.site.register(CronJob, CronJobAdmin)
