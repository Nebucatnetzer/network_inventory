from django.contrib import admin

# Register your models here.

from .models import (
    ComputerLicense,
    LicenseWithComputer,
    UserLicense,
)


class LicenseWithComputerAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class UserLicenseAdmin(admin.ModelAdmin):
    model = UserLicense
    extra = 0
    verbose_name_plural = 'User Licenses'


class ComputerLicenseAdmin(admin.ModelAdmin):
    model = ComputerLicense
    extra = 0
    verbose_name_plural = 'Computer Licenses'


admin.site.register(ComputerLicense, ComputerLicenseAdmin)
admin.site.register(LicenseWithComputer, LicenseWithComputerAdmin)
admin.site.register(UserLicense, UserLicenseAdmin)
