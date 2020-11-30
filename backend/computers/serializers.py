from rest_framework import serializers

from .models import Computer
from .models import ComputerCpuRelation
from .models import ComputerDiskRelation
from .models import ComputerGpuRelation
from .models import ComputerRamRelation
from .models import ComputerSoftwareRelation
from .models import CpuArchitecture
from .models import CpuManufacturer
from .models import Cpu
from .models import DiskType
from .models import Disk
from .models import GpuManufacturer
from .models import Gpu
from .models import DisksInRaid
from .models import RaidType
from .models import Raid
from .models import RamType
from .models import Ram


class ComputerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Computer
        fields = '__all__'


class ComputerCpuRelationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComputerCpuRelation
        fields = '__all__'


class ComputerDiskRelationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComputerDiskRelation
        fields = '__all__'


class ComputerGpuRelationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComputerGpuRelation
        fields = '__all__'


class ComputerRamRelationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComputerRamRelation
        fields = '__all__'


class ComputerSoftwareRelationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComputerSoftwareRelation
        fields = '__all__'


class CpuArchitectureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CpuArchitecture
        fields = '__all__'


class CpuManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CpuManufacturer
        fields = '__all__'


class CpuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cpu
        fields = '__all__'


class DiskTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiskType
        fields = '__all__'


class DiskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disk
        fields = '__all__'


class GpuManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GpuManufacturer
        fields = '__all__'


class GpuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gpu
        fields = '__all__'


class DisksInRaidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DisksInRaid
        fields = '__all__'


class RaidTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RaidType
        fields = '__all__'


class RaidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Raid
        fields = '__all__'


class RamTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RamType
        fields = '__all__'


class RamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ram
        fields = '__all__'
