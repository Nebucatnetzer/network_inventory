from rest_framework import serializers

from .models import Owner
from .models import Customer
from .models import DeviceManufacturer
from .models import Location


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class DeviceManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeviceManufacturer
        fields = '__all__'


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
