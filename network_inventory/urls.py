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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", include("backups.urls")),
    path(r"", include("computers.urls")),
    path(r"", include("core.urls")),
    path(r"", include("customers.urls")),
    path(r"", include("devices.urls")),
    path(r"", include("licenses.urls")),
    path(r"", include("nets.urls")),
    path(r"", include("users.urls")),
    path("management/", admin.site.urls),
    path("_nested_admin/", include("nested_admin.urls")),
]
