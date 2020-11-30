from rest_framework import viewsets
from rest_framework import permissions

from .models import OperatingSystem
from .models import SoftwareArchitecture
from .models import SoftwareCategory
from .models import Software

from .serializers import OperatingSystemSerializer
from .serializers import SoftwareArchitectureSerializer
from .serializers import SoftwareCategorySerializer
from .serializers import SoftwareSerializer


class OperatingSystemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = OperatingSystem.objects.all()
    serializer_class = OperatingSystemSerializer
    permission_classes = [permissions.IsAuthenticated]


class SoftwareArchitectureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = SoftwareArchitecture.objects.all()
    serializer_class = SoftwareArchitectureSerializer
    permission_classes = [permissions.IsAuthenticated]


class SoftwareCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = SoftwareCategory.objects.all()
    serializer_class = SoftwareCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class SoftwareViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
    permission_classes = [permissions.IsAuthenticated]




