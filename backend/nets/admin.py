from django.contrib import admin


from .models import (
    IpStatus,
    Net,
)


admin.site.register(IpStatus)
admin.site.register(Net)
