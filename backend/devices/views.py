from rest_framework import viewsets
from rest_framework import permissions

from .models import Warranty
from .models import WarrantyType
from .models import Device
from .models import DeviceCategory
from .models import DeviceInNet
from .models import DeviceManufacturer
from .models import HardwareModel

from .serializers import WarrantySerializer
from .serializers import WarrantyTypeSerializer
from .serializers import DeviceSerializer
from .serializers import DeviceCategorySerializer
from .serializers import DeviceInNetSerializer
from .serializers import DeviceManufacturerSerializer
from .serializers import HardwareModelSerializer


class WarrantyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = Warranty.objects.all()
    serializer_class = WarrantySerializer
    permission_classes = [permissions.IsAuthenticated]


class WarrantyTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = WarrantyType.objects.all()
    serializer_class = WarrantyTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = Device.objects.all().order_by('name')
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeviceCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = DeviceCategory.objects.all()
    serializer_class = DeviceCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class DeviceInNetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = DeviceInNet.objects.all()
    serializer_class = DeviceInNetSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeviceManufacturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = DeviceManufacturer.objects.all()
    serializer_class = DeviceManufacturerSerializer
    permission_classes = [permissions.IsAuthenticated]


class HardwareModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = HardwareModel.objects.all()
    serializer_class = HardwareModelSerializer
    permission_classes = [permissions.IsAuthenticated]
