from django.contrib import admin


from .models import (
    IpStatus,
    Net,
)


class IpStatusAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.register(IpStatus, IpStatusAdmin)
admin.site.register(Net)
