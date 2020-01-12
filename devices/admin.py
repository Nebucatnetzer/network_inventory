from django.contrib import admin
import nested_admin

from .models import (
    ConnectedDevice,
    Device,
    DeviceCategory,
    DeviceInNet,
    DeviceManufacturer,
    Warranty,
    WarrantyType
)


class DeviceCategoryAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class DeviceManufacturerAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class DeviceInNetInline(nested_admin.NestedStackedInline):
    model = DeviceInNet
    extra = 0
    verbose_name_plural = 'Nets'


class WarrantyTypeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.register(ConnectedDevice)
admin.site.register(Device)
admin.site.register(DeviceCategory, DeviceCategoryAdmin)
admin.site.register(DeviceInNet)
admin.site.register(DeviceManufacturer, DeviceManufacturerAdmin)
admin.site.register(Warranty)
admin.site.register(WarrantyType, WarrantyTypeAdmin)
