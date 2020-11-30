from rest_framework import viewsets
from rest_framework import permissions

from .models import IpStatus
from .models import Net

from .serializers import IpStatusSerializer
from .serializers import NetSerializer


class IpStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = IpStatus.objects.all()
    serializer_class = IpStatusSerializer
    permission_classes = [permissions.IsAuthenticated]


class NetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = Net.objects.all()
    serializer_class = NetSerializer
    permission_classes = [permissions.IsAuthenticated]
