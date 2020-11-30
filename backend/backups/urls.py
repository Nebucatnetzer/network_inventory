from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'backup-methods',
                views.BackupMethodViewSet,
                'backup-method')
router.register(r'backups', views.BackupViewSet)
router.register(r'target-devices',
                views.TargetDeviceViewSet,
                'target-device')
router.register(r'notifications-from-backup',
                views.NotificationFromBackupViewSet,
                'notification-from-backup')
router.register(r'notifications',
                views.NotificationViewSet)
router.register(r'notifications-type',
                views.NotificationTypeViewSet,
                'notification-types')


urlpatterns = [
    # required for the login functionality
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]
