from django.urls import path, include

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'owners', views.OwnerViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'device-manufacturers',
                views.DeviceManufacturerViewSet,
                'device-manufacturer')
router.register(r'locations', views.LocationViewSet)


urlpatterns = [
    # required for the login functionality
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]
