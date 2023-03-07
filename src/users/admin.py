from django.contrib import admin

from licenses.models import LicenseWithUser

from .models import (
    Group,
    Login,
    LoginInGroup,
    MailAlias,
    User,
)


class LicenseWithUserInLine(admin.StackedInline):
    model = LicenseWithUser
    extra = 0
    verbose_name_plural = "Licenses"


class GroupInLine(admin.StackedInline):
    model = LoginInGroup
    extra = 0
    verbose_name_plural = "Groups"


class MailAliasInLine(admin.StackedInline):
    model = MailAlias
    extra = 0
    verbose_name_plural = "Mail Aliases"


class LoginAdmin(admin.ModelAdmin):
    list_display = ("login", "enabled")
    inlines = (GroupInLine,)


class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "customer")
    inlines = (
        MailAliasInLine,
        LicenseWithUserInLine,
    )


admin.site.register(Group)
admin.site.register(MailAlias)
admin.site.register(User, UserAdmin)
admin.site.register(Login, LoginAdmin)
admin.site.register(LoginInGroup)
