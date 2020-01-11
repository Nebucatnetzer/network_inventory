from django.contrib import admin
import nested_admin

from devices.models import DeviceInNet

from .models import (
    Backup,
    BackupMethod,
    Computer,
    ComputerCpuRelation,
    ComputerDiskRelation,
    ComputerLicense,
    ComputerRamRelation,
    ComputerSoftwareRelation,
    Cpu,
    CpuArchitecture,
    CpuManufacturer,
    Disk,
    DiskType,
    DisksInRaid,
    LicenseWithComputer,
    LicenseWithUser,
    Notification,
    NotificationType,
    NotificationFromBackup,
    OperatingSystem,
    Raid,
    RaidType,
    Ram,
    RamType,
    Software,
    SoftwareArchitecture,
    SoftwareCategory,
    TargetDevice,
    UserLicense,
    Warranty,
    WarrantyType
)


class CpuAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class CpuArchitectureAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class BackupMethodAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class CpuManufacturerAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class IpStatusAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class LicenseWithComputerAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class NotificationTypeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class NotificationAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class OperatingSystemAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class RamModuleAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class RaidTypeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class SoftwareArchitectureAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class SoftwareCategoryAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class TargetDeviceAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class DiskTypeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class RamTypeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class WarrantyTypeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class DiskInRaidAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class SoftwareInLine(nested_admin.NestedStackedInline):
    model = ComputerSoftwareRelation
    extra = 0
    verbose_name_plural = 'Software'


class RamInLine(nested_admin.NestedStackedInline):
    model = ComputerRamRelation
    extra = 0
    verbose_name_plural = 'RAM Modules'


class DiskInLine(nested_admin.NestedStackedInline):
    model = ComputerDiskRelation
    extra = 0
    verbose_name_plural = 'Disks'


class DisksInRaidInLine(nested_admin.NestedStackedInline):
    model = DisksInRaid
    extra = 0
    verbose_name_plural = 'Disks in RAID'


class CpusInLine(nested_admin.NestedStackedInline):
    model = ComputerCpuRelation
    extra = 0
    verbose_name_plural = 'CPUs'


class RaidInLine(nested_admin.NestedStackedInline):
    model = Raid
    extra = 0
    verbose_name_plural = 'RAID'
    inlines = (DisksInRaidInLine,)


class DeviceInNetInline(nested_admin.NestedStackedInline):
    model = DeviceInNet
    extra = 0
    verbose_name_plural = 'Nets'


class LicenseWithComputerInLine(nested_admin.NestedStackedInline):
    model = LicenseWithComputer
    extra = 0
    verbose_name_plural = 'Licenses'


class ComputerAdmin(nested_admin.NestedModelAdmin):
    list_display = ('name', 'host')
    inlines = (SoftwareInLine, CpusInLine, RamInLine, DiskInLine, RaidInLine,
               DeviceInNetInline, LicenseWithComputerInLine)


class TargetDeviceInLine(admin.StackedInline):
    model = TargetDevice
    extra = 0
    verbose_name_plural = 'Target Devices'


class NotificationForBackupInLine(admin.StackedInline):
    model = NotificationFromBackup
    extra = 0
    verbose_name_plural = 'Notifications'


class BackupAdmin(admin.ModelAdmin):
    inlines = (TargetDeviceInLine, NotificationForBackupInLine)


class UserLicenseAdmin(admin.ModelAdmin):
    model = UserLicense
    extra = 0
    verbose_name_plural = 'User Licenses'


class ComputerLicenseAdmin(admin.ModelAdmin):
    model = ComputerLicense
    extra = 0
    verbose_name_plural = 'Computer Licenses'


admin.site.register(Backup, BackupAdmin)
admin.site.register(BackupMethod, BackupMethodAdmin)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(ComputerLicense, ComputerLicenseAdmin)
admin.site.register(Cpu, CpuAdmin)
admin.site.register(CpuArchitecture, CpuArchitectureAdmin)
admin.site.register(CpuManufacturer, CpuManufacturerAdmin)
admin.site.register(Disk)
admin.site.register(DiskType, DiskTypeAdmin)
admin.site.register(LicenseWithComputer, LicenseWithComputerAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(NotificationType, NotificationTypeAdmin)
admin.site.register(OperatingSystem, OperatingSystemAdmin)
admin.site.register(RaidType, RaidTypeAdmin)
admin.site.register(Ram, RamModuleAdmin)
admin.site.register(RamType, RamTypeAdmin)
admin.site.register(Software)
admin.site.register(SoftwareArchitecture, SoftwareArchitectureAdmin)
admin.site.register(SoftwareCategory, SoftwareCategoryAdmin)
admin.site.register(TargetDevice, TargetDeviceAdmin)
admin.site.register(UserLicense, UserLicenseAdmin)
admin.site.register(Warranty)
admin.site.register(WarrantyType, WarrantyTypeAdmin)