from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'ip-status', views.IpStatusViewSet)
router.register(r'nets', views.NetViewSet)


urlpatterns = [
    # required for the login functionality
    path('api/', include(router.urls)),
]
