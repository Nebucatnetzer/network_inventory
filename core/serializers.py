from rest_framework import serializers

from .models import Weekday
from .models import Month
from .models import DayOfMonth


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
