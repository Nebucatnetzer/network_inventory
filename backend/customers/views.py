from rest_framework import viewsets
from rest_framework import permissions

from .models import Owner
from .models import Customer
from .models import DeviceManufacturer
from .models import Location

from .serializers import OwnerSerializer
from .serializers import CustomerSerializer
from .serializers import DeviceManufacturerSerializer
from .serializers import LocationSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [permissions.IsAuthenticated]


class DeviceManufacturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = DeviceManufacturer.objects.all()
    serializer_class = DeviceManufacturerSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = Location.objects.all().order_by('name')
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]
