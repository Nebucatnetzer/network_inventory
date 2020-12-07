from rest_framework import viewsets
from rest_framework import permissions

from .models import Weekday
from .models import Month
from .models import DayOfMonth
from .models import HoursInDay
from .models import MinutesInHour

from .serializers import WeekdaySerializer
from .serializers import MonthSerializer
from .serializers import DayOfMonthSerializer
from .serializers import HoursInDaySerializer
from .serializers import MinutesInHourSerializer


class WeekdayViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows weekdays to be viewed or edited.
    """
    queryset = Weekday.objects.all()
    serializer_class = WeekdaySerializer
    permission_classes = [permissions.IsAuthenticated]


class MonthViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows months to be viewed or edited.
    """
    queryset = Month.objects.all()
    serializer_class = MonthSerializer
    permission_classes = [permissions.IsAuthenticated]


class DayOfMonthViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows day of months to be viewed or edited.
    """
    queryset = DayOfMonth.objects.all()
    serializer_class = DayOfMonthSerializer
    permission_classes = [permissions.IsAuthenticated]


class HoursInDayViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows hours in day to be viewed or edited.
    """
    queryset = HoursInDay.objects.all()
    serializer_class = HoursInDaySerializer
    permission_classes = [permissions.IsAuthenticated]


class MinutesInHourViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows minutes in hour to be viewed or edited.
    """
    queryset = MinutesInHour.objects.all()
    serializer_class = MinutesInHourSerializer
    permission_classes = [permissions.IsAuthenticated]
