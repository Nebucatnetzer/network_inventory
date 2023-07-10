from django.contrib import admin
import nested_admin

from devices.models import DeviceInNet
from licenses.models import LicenseWithComputer

from .models import (
    Computer,
    ComputerCpuRelation,
    ComputerDiskRelation,
    ComputerGpuRelation,
    ComputerRamRelation,
    ComputerSoftwareRelation,
    Cpu,
    CpuArchitecture,
    CpuManufacturer,
    Disk,
    DiskType,
    DisksInRaid,
    Gpu,
    GpuManufacturer,
    Raid,
    RaidType,
    Ram,
    RamType,
)


class SoftwareInLine(nested_admin.NestedStackedInline):  # pylint: disable=no-member
    model = ComputerSoftwareRelation
    extra = 0
    verbose_name_plural = "Software"


class RamInLine(nested_admin.NestedStackedInline):  # pylint: disable=no-member
    model = ComputerRamRelation
    extra = 0
    verbose_name_plural = "RAM Modules"


class DiskInLine(nested_admin.NestedStackedInline):  # pylint: disable=no-member
    model = ComputerDiskRelation
    extra = 0
    verbose_name_plural = "Disks"


class DisksInRaidInLine(nested_admin.NestedStackedInline):  # pylint: disable=no-member
    model = DisksInRaid
    extra = 0
    verbose_name_plural = "Disks in RAID"


class CpusInLine(nested_admin.NestedStackedInline):  # pylint: disable=no-member
    model = ComputerCpuRelation
    extra = 0
    verbose_name_plural = "CPUs"


class GpusInLine(nested_admin.NestedStackedInline):  # pylint: disable=no-member
    model = ComputerGpuRelation
    extra = 0
    verbose_name_plural = "GPUs"


class RaidInLine(nested_admin.NestedStackedInline):  # pylint: disable=no-member
    model = Raid
    extra = 0
    verbose_name_plural = "RAID"
    inlines = (DisksInRaidInLine,)


class DeviceInNetInline(nested_admin.NestedStackedInline):  # pylint: disable=no-member
    model = DeviceInNet
    extra = 0
    verbose_name_plural = "Nets"


class LicenseWithComputerInLine(
    nested_admin.NestedStackedInline
):  # pylint: disable=no-member
    model = LicenseWithComputer
    extra = 0
    verbose_name_plural = "Licenses"


class ComputerAdmin(nested_admin.NestedModelAdmin):  # pylint: disable=no-member
    list_display = ("name", "host")
    inlines = (
        SoftwareInLine,
        CpusInLine,
        GpusInLine,
        RamInLine,
        DiskInLine,
        RaidInLine,
        DeviceInNetInline,
        LicenseWithComputerInLine,
    )


admin.site.register(Computer, ComputerAdmin)
admin.site.register(Cpu)
admin.site.register(CpuArchitecture)
admin.site.register(CpuManufacturer)
admin.site.register(Disk)
admin.site.register(DiskType)
admin.site.register(Gpu)
admin.site.register(GpuManufacturer)
admin.site.register(RaidType)
admin.site.register(Ram)
admin.site.register(RamType)
