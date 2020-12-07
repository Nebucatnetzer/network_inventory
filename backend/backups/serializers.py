from rest_framework import serializers

from .models import BackupMethod
from .models import Backup
from .models import TargetDevice
from .models import NotificationFromBackup
from .models import Notification
from .models import NotificationType


class BackupMethodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BackupMethod
        fields = '__all__'


class BackupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Backup
        fields = '__all__'


class TargetDeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TargetDevice
        fields = '__all__'


class NotificationFromBackupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NotificationFromBackup
        fields = '__all__'


class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class NotificationTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NotificationType
        fields = '__all__'
