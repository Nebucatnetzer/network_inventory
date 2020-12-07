from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'warranties', views.WarrantyViewSet)
router.register(r'warranty-types', views.WarrantyTypeViewSet)
router.register(r'devices', views.DeviceViewSet)
router.register(r'device-categories', views.DeviceCategoryViewSet)
router.register(r'devices-in-net', views.DeviceInNetViewSet)
router.register(r'device-manufacturers', views.DeviceManufacturerViewSet)
router.register(r'hardware-models', views.HardwareModelViewSet)
