from rest_framework import serializers

from .models import Weekday
from .models import Month
from .models import DayOfMonth
from .models import HoursInDay
from .models import MinutesInHour


class WeekdaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weekday
        fields = '__all__'


class MonthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Month
        fields = '__all__'


class DayOfMonthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DayOfMonth
        fields = '__all__'


class HoursInDaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HoursInDay
        fields = '__all__'


class MinutesInHourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MinutesInHour
        fields = '__all__'
