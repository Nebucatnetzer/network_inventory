from django.urls import path, include

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'months', views.MonthViewSet)
router.register(r'weekdays', views.WeekdayViewSet)
router.register(r'days-of-month',
                views.DayOfMonthViewSet,
                'days-of-month')
router.register(r'hours-in-day',
                views.HoursInDayViewSet,
                'hours-in-day')
router.register(r'minutes-in-hour',
                views.MinutesInHourViewSet,
                'minutes-in-hour')


urlpatterns = [
    # required for the login functionality
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]
