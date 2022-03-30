from django.contrib import admin

from licenses.models import LicenseWithUser

from .models import (
    Group,
    MailAlias,
    User,
    UserInGroup,
)


class LicenseWithUserInLine(admin.StackedInline):
    model = LicenseWithUser
    extra = 0
    verbose_name_plural = "Licenses"


class GroupInLine(admin.StackedInline):
    model = UserInGroup
    extra = 0
    verbose_name_plural = "AD Groups"


class MailAliasInLine(admin.StackedInline):
    model = MailAlias
    extra = 0
    verbose_name_plural = "Mail Aliases"


class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "customer", "enabled")
    inlines = (
        GroupInLine,
        MailAliasInLine,
        LicenseWithUserInLine,
    )


admin.site.register(Group)
admin.site.register(MailAlias)
admin.site.register(User, UserAdmin)
admin.site.register(UserInGroup)
