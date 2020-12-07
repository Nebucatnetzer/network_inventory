from rest_framework import serializers

from .models import OperatingSystem
from .models import SoftwareArchitecture
from .models import SoftwareCategory
from .models import Software


class OperatingSystemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OperatingSystem
        fields = '__all__'


class SoftwareArchitectureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SoftwareArchitecture
        fields = '__all__'


class SoftwareCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SoftwareCategory
        fields = '__all__'


class SoftwareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Software
        fields = '__all__'
