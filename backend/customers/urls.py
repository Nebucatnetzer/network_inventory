from django.urls import path, include

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'owners', views.OwnerViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'device-manufacturers', views.DeviceManufacturerViewSet)
router.register(r'locations', views.LocationViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]
