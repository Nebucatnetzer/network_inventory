"""network_inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from backups.urls import router as backups_router
from computers.urls import router as computers_router
from core.urls import router as core_router
from customers.urls import router as customers_router
from devices.urls import router as devices_router
from licenses.urls import router as licenses_router
from nets.urls import router as nets_router
from softwares.urls import router as softwares_router
from users.urls import router as users_router


router = routers.DefaultRouter()
router.registry.extend(backups_router.registry)
router.registry.extend(computers_router.registry)
router.registry.extend(core_router.registry)
router.registry.extend(customers_router.registry)
router.registry.extend(devices_router.registry)
router.registry.extend(licenses_router.registry)
router.registry.extend(nets_router.registry)
router.registry.extend(softwares_router.registry)
router.registry.extend(users_router.registry)


urlpatterns = [
    #path(r'^_nested_admin/', include('nested_admin.urls')),
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls')),
    path('api/admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
