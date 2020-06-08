from django.contrib import admin

from .models import (
    Backup,
    BackupMethod,
    Notification,
    NotificationType,
    NotificationFromBackup,
    TargetDevice,
)


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


admin.site.register(Backup, BackupAdmin)
admin.site.register(BackupMethod)
admin.site.register(Notification)
admin.site.register(NotificationType)
admin.site.register(TargetDevice)
