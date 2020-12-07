from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'backup-methods', views.BackupMethodViewSet)
router.register(r'backups', views.BackupViewSet)
router.register(r'target-devices', views.TargetDeviceViewSet)
router.register(r'notifications-from-backup',
                views.NotificationFromBackupViewSet)
router.register(r'notifications', views.NotificationViewSet)
router.register(r'notifications-type', views.NotificationTypeViewSet,)
