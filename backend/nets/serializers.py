from rest_framework import serializers

from .models import IpStatus
from .models import Net


class IpStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IpStatus
        fields = '__all__'


class NetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Net
        fields = '__all__'
