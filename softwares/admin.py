from django.contrib import admin

# Register your models here.

from .models import (
    OperatingSystem,
    Software,
    SoftwareArchitecture,
    SoftwareCategory,
)


class OperatingSystemAdmin(admin.ModelAdmin):
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


admin.site.register(OperatingSystem, OperatingSystemAdmin)
admin.site.register(Software)
admin.site.register(SoftwareArchitecture, SoftwareArchitectureAdmin)
admin.site.register(SoftwareCategory, SoftwareCategoryAdmin)
