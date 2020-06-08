from django.contrib import admin

from licenses.models import LicenseWithUser

from .models import (
    AdGroup,
    MailAlias,
    MailGroup,
    User,
    UserInAdGroup,
    UserInMailGroup,
)


class LicenseWithUserInLine(admin.StackedInline):
    model = LicenseWithUser
    extra = 0
    verbose_name_plural = 'Licenses'


class AdGroupInLine(admin.StackedInline):
    model = UserInAdGroup
    extra = 0
    verbose_name_plural = 'AD Groups'


class MailGroupInLine(admin.StackedInline):
    model = UserInMailGroup
    extra = 0
    verbose_name_plural = 'Mail Groups'


class MailAliasInLine(admin.StackedInline):
    model = MailAlias
    extra = 0
    verbose_name_plural = 'Mail Aliases'


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'customer', 'enabled')
    inlines = (AdGroupInLine,
               MailGroupInLine,
               MailAliasInLine,
               LicenseWithUserInLine)


admin.site.register(AdGroup)
admin.site.register(MailAlias)
admin.site.register(MailGroup)
admin.site.register(User, UserAdmin)
admin.site.register(UserInAdGroup)
admin.site.register(UserInMailGroup)
