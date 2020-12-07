from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'operating-systems', views.OperatingSystemViewSet)
router.register(r'software-architectures', views.SoftwareArchitectureViewSet)
router.register(r'software-categories', views.SoftwareCategoryViewSet)
router.register(r'softwares', views.SoftwareViewSet)
