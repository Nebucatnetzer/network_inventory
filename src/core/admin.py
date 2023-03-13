from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import InventoryUser
from .models import Service

admin.site.register(InventoryUser, UserAdmin)
admin.site.register(Service)
