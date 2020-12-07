from rest_framework import viewsets
from rest_framework import permissions

from .models import BackupMethod
from .models import Backup
from .models import TargetDevice
from .models import NotificationFromBackup
from .models import Notification
from .models import NotificationType

from .serializers import BackupMethodSerializer
from .serializers import BackupSerializer
from .serializers import TargetDeviceSerializer
from .serializers import NotificationFromBackupSerializer
from .serializers import NotificationSerializer
from .serializers import NotificationTypeSerializer


class BackupMethodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BackupMethods to be viewed or edited.
    """
    queryset = BackupMethod.objects.all()
    serializer_class = BackupMethodSerializer
    permission_classes = [permissions.IsAuthenticated]


class BackupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BackupMethods to be viewed or edited.
    """
    queryset = Backup.objects.all().order_by('name')
    serializer_class = BackupSerializer
    permission_classes = [permissions.IsAuthenticated]


class TargetDeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BackupMethods to be viewed or edited.
    """
    queryset = TargetDevice.objects.all().order_by('device')
    serializer_class = TargetDeviceSerializer
    permission_classes = [permissions.IsAuthenticated]


class NotificationFromBackupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BackupMethods to be viewed or edited.
    """
    queryset = NotificationFromBackup.objects.all().order_by('backup')
    serializer_class = NotificationFromBackupSerializer
    permission_classes = [permissions.IsAuthenticated]


class NotificationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BackupMethods to be viewed or edited.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]


class NotificationTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BackupMethods to be viewed or edited.
    """
    queryset = NotificationType.objects.all().order_by('name')
    serializer_class = NotificationTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
