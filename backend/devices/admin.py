from django.contrib import admin
import nested_admin

from .models import (
    Device,
    DeviceCategory,
    DeviceInNet,
    DeviceManufacturer,
    HardwareModel,
    Warranty,
    WarrantyType
)


class DeviceInNetInline(nested_admin.NestedStackedInline):
    model = DeviceInNet
    extra = 0
    verbose_name_plural = 'Nets'


class DeviceAdmin(nested_admin.NestedModelAdmin):
    inlines = (DeviceInNetInline, )


admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceCategory)
admin.site.register(DeviceInNet)
admin.site.register(DeviceManufacturer)
admin.site.register(HardwareModel)
admin.site.register(Warranty)
admin.site.register(WarrantyType)
