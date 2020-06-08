from django.contrib import admin

# Register your models here.

from .models import (
    ComputerLicense,
    LicenseWithComputer,
    UserLicense,
)


class UserLicenseAdmin(admin.ModelAdmin):
    model = UserLicense
    extra = 0
    verbose_name_plural = 'User Licenses'


class ComputerLicenseAdmin(admin.ModelAdmin):
    model = ComputerLicense
    extra = 0
    verbose_name_plural = 'Computer Licenses'


admin.site.register(ComputerLicense, ComputerLicenseAdmin)
admin.site.register(LicenseWithComputer)
admin.site.register(UserLicense, UserLicenseAdmin)
