from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'warranties', views.WarrantyViewSet)
router.register(r'warranty-types',
                views.WarrantyTypeViewSet,
                'warranty-type')
router.register(r'devices', views.DeviceViewSet)
router.register(r'device-categories',
                views.DeviceCategoryViewSet,
                'device-category')
router.register(r'devices-in-net',
                views.DeviceInNetViewSet,
                'device-in-net')
router.register(r'device-manufacturers',
                views.DeviceManufacturerViewSet,
                'device-manufacturer')
router.register(r'hardware-models',
                views.HardwareModelViewSet,
                'hardware-model')


urlpatterns = [
    # required for the login functionality
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]
