from django.contrib import admin

# Register your models here.

from .models import (
    OperatingSystem,
    Software,
    SoftwareArchitecture,
    SoftwareCategory,
)


admin.site.register(OperatingSystem)
admin.site.register(Software)
admin.site.register(SoftwareArchitecture)
admin.site.register(SoftwareCategory)
