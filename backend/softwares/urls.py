from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'operating-systems',
                views.OperatingSystemViewSet,
                'operating-system')
router.register(r'software-architectures',
                views.SoftwareArchitectureViewSet,
                'software-architecture')
router.register(r'software-categories',
                views.SoftwareCategoryViewSet,
                'software-category')
router.register(r'softwares', views.SoftwareViewSet)


urlpatterns = [
    # required for the login functionality
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]
