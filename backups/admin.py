from django.contrib import admin

from .models import (
    Backup,
    BackupMethod,
    Notification,
    NotificationType,
    NotificationFromBackup,
    TargetDevice,
)


class BackupMethodAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class NotificationTypeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class NotificationAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class TargetDeviceInLine(admin.StackedInline):
    model = TargetDevice
    extra = 0
    verbose_name_plural = 'Target Devices'


class NotificationForBackupInLine(admin.StackedInline):
    model = NotificationFromBackup
    extra = 0
    verbose_name_plural = 'Notifications'


class BackupAdmin(admin.ModelAdmin):
    inlines = (TargetDeviceInLine, NotificationForBackupInLine)


class TargetDeviceAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.register(Backup, BackupAdmin)
admin.site.register(BackupMethod, BackupMethodAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(NotificationType, NotificationTypeAdmin)
admin.site.register(TargetDevice, TargetDeviceAdmin)
