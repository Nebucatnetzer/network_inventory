from django.urls import path, include

from rest_framework import routers

from core import views as core_views


router = routers.DefaultRouter()
router.register(r'months', core_views.MonthViewSet)
router.register(r'weekdays', core_views.WeekdayViewSet)
router.register(r'days-of-month',
                core_views.DayOfMonthViewSet,
                'days-of-month')
router.register(r'hours-in-day',
                core_views.HoursInDayViewSet,
                'hours-in-day')
router.register(r'minutes-in-hour',
                core_views.MinutesInHourViewSet,
                'minutes-in-hour')


urlpatterns = [
    # required for the login functionality
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]
