from django.urls import path, include

from rest_framework import routers


router = routers.DefaultRouter()


urlpatterns = [
    # required for the login functionality
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]
