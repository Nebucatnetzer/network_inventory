from rest_framework import viewsets
from rest_framework import permissions

from .models import UserLicense
from .models import ComputerLicense
from .models import LicenseWithUser
from .models import LicenseWithComputer

from .serializers import UserLicenseSerializer
from .serializers import ComputerLicenseSerializer
from .serializers import LicenseWithUserSerializer
from .serializers import LicenseWithComputerSerializer


class UserLicenseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = UserLicense.objects.all()
    serializer_class = UserLicenseSerializer
    permission_classes = [permissions.IsAuthenticated]


class ComputerLicenseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = ComputerLicense.objects.all()
    serializer_class = ComputerLicenseSerializer
    permission_classes = [permissions.IsAuthenticated]


class LicenseWithUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = LicenseWithUser.objects.all().order_by('user')
    serializer_class = LicenseWithUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class LicenseWithComputerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = LicenseWithComputer.objects.all().order_by('computer')
    serializer_class = LicenseWithComputerSerializer
    permission_classes = [permissions.IsAuthenticated]
