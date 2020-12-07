from rest_framework import viewsets
from rest_framework import permissions

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

from .serializers import ComputerSerializer
from .serializers import ComputerCpuRelationSerializer
from .serializers import ComputerDiskRelationSerializer
from .serializers import ComputerGpuRelationSerializer
from .serializers import ComputerRamRelationSerializer
from .serializers import ComputerSoftwareRelationSerializer
from .serializers import CpuArchitectureSerializer
from .serializers import CpuManufacturerSerializer
from .serializers import CpuSerializer
from .serializers import DiskTypeSerializer
from .serializers import DiskSerializer
from .serializers import GpuManufacturerSerializer
from .serializers import GpuSerializer
from .serializers import DisksInRaidSerializer
from .serializers import RaidTypeSerializer
from .serializers import RaidSerializer
from .serializers import RamTypeSerializer
from .serializers import RamSerializer


class ComputerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = Computer.objects.all().order_by('name')
    serializer_class = ComputerSerializer
    permission_classes = [permissions.IsAuthenticated]


class ComputerCpuRelationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = ComputerCpuRelation.objects.all().order_by('computer')
    serializer_class = ComputerCpuRelationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ComputerDiskRelationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = ComputerDiskRelation.objects.all().order_by('computer')
    serializer_class = ComputerDiskRelationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ComputerGpuRelationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = ComputerGpuRelation.objects.all().order_by('computer')
    serializer_class = ComputerGpuRelationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ComputerRamRelationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = ComputerRamRelation.objects.all().order_by('computer')
    serializer_class = ComputerRamRelationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ComputerSoftwareRelationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = ComputerSoftwareRelation.objects.all().order_by('computer')
    serializer_class = ComputerSoftwareRelationSerializer
    permission_classes = [permissions.IsAuthenticated]


class CpuArchitectureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = CpuArchitecture.objects.all().order_by('name')
    serializer_class = CpuArchitectureSerializer
    permission_classes = [permissions.IsAuthenticated]


class CpuManufacturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = CpuManufacturer.objects.all().order_by('name')
    serializer_class = CpuManufacturerSerializer
    permission_classes = [permissions.IsAuthenticated]


class CpuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = Cpu.objects.all().order_by('name')
    serializer_class = CpuSerializer
    permission_classes = [permissions.IsAuthenticated]


class DiskTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = DiskType.objects.all()
    serializer_class = DiskTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class DiskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = Disk.objects.all().order_by('computer')
    serializer_class = DiskSerializer
    permission_classes = [permissions.IsAuthenticated]


class GpuManufacturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = GpuManufacturer.objects.all().order_by('name')
    serializer_class = GpuManufacturerSerializer
    permission_classes = [permissions.IsAuthenticated]


class GpuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = Gpu.objects.all().order_by('name')
    serializer_class = GpuSerializer
    permission_classes = [permissions.IsAuthenticated]


class DisksInRaidViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = DisksInRaid.objects.all().order_by('raid')
    serializer_class = DisksInRaidSerializer
    permission_classes = [permissions.IsAuthenticated]


class RaidTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = RaidType.objects.all().order_by('name')
    serializer_class = RaidTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class RaidViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = Raid.objects.all().order_by('computer')
    serializer_class = RaidSerializer
    permission_classes = [permissions.IsAuthenticated]


class RamTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = RamType.objects.all().order_by('name')
    serializer_class = RamTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class RamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = Ram.objects.all().order_by('computer')
    serializer_class = RamSerializer
    permission_classes = [permissions.IsAuthenticated]
