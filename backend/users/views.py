from rest_framework import viewsets
from rest_framework import permissions

from .models import User
from .models import UserInAdGroup
from .models import UserInMailGroup
from .models import AdGroup
from .models import MailGroup
from .models import MailAlias

from .serializers import UserSerializer
from .serializers import UserInAdGroupSerializer
from .serializers import UserInMailGroupSerializer
from .serializers import AdGroupSerializer
from .serializers import MailGroupSerializer
from .serializers import MailAliasSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserInAdGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = UserInAdGroup.objects.all()
    serializer_class = UserInAdGroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserInMailGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = UserInMailGroup.objects.all()
    serializer_class = UserInMailGroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class AdGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = AdGroup.objects.all()
    serializer_class = AdGroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class MailGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = MailGroup.objects.all()
    serializer_class = MailGroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class MailAliasViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = MailAlias.objects.all()
    serializer_class = MailAliasSerializer
    permission_classes = [permissions.IsAuthenticated]
