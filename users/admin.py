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


class MailAliasAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class UserInAdGroupAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class UserInMailGroupAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


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
    inlines = (AdGroupInLine, MailGroupInLine, MailAliasInLine, LicenseWithUserInLine)


admin.site.register(AdGroup)
admin.site.register(MailAlias, MailAliasAdmin)
admin.site.register(MailGroup)
admin.site.register(User, UserAdmin)
admin.site.register(UserInAdGroup, UserInAdGroupAdmin)
admin.site.register(UserInMailGroup, UserInMailGroupAdmin)
