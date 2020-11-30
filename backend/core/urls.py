from django.urls import path, include

from rest_framework import routers

from core import views as core_views


router = routers.DefaultRouter()
router.register(r'months', core_views.MonthViewSet)
router.register(r'weekdays', core_views.WeekdayViewSet)
router.register(r'day-of-months', core_views.DayOfMonthViewSet)
router.register(r'hoursinday', core_views.HoursInDayViewSet)
router.register(r'minutesinhour', core_views.MinutesInHourViewSet)


urlpatterns = [
    # required for the login functionality
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]
