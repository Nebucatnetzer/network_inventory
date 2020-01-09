from django.contrib import admin

from guardian.admin import GuardedModelAdmin

from .models import Customer, Owner


class CustomerAdmin(GuardedModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Owner)
