from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'user-licenses',
                views.UserLicenseViewSet,
                'user-license')
router.register(r'computer-licenses',
                views.ComputerLicenseViewSet,
                'computer-license')
router.register(r'licenses-with-user',
                views.LicenseWithUserViewSet,
                'license-with-user')
router.register(r'licenses-with-computer',
                views.LicenseWithComputerViewSet,
                'license-with-computer')


urlpatterns = [
    # required for the login functionality
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]
