from rest_framework import serializers

from .models import Warranty
from .models import WarrantyType
from .models import Device
from .models import DeviceCategory
from .models import DeviceInNet
from .models import DeviceManufacturer
from .models import HardwareModel


class WarrantySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Warranty
        fields = '__all__'


class WarrantyTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WarrantyType
        fields = '__all__'


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class DeviceCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeviceCategory
        fields = '__all__'


class DeviceInNetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeviceInNet
        fields = '__all__'


class DeviceManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeviceManufacturer
        fields = '__all__'


class HardwareModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HardwareModel
        fields = '__all__'
