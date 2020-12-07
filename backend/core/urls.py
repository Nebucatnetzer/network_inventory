from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'months', views.MonthViewSet)
router.register(r'weekdays', views.WeekdayViewSet)
router.register(r'days-of-month', views.DayOfMonthViewSet)
router.register(r'hours-in-day', views.HoursInDayViewSet)
router.register(r'minutes-in-hour', views.MinutesInHourViewSet)
