from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'user-licenses', views.UserLicenseViewSet)
router.register(r'computer-licenses', views.ComputerLicenseViewSet)
router.register(r'licenses-with-user', views.LicenseWithUserViewSet)
router.register(r'licenses-with-computer', views.LicenseWithComputerViewSet)
