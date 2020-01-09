from django.urls import path

from . import views


urlpatterns = [
    path('customer/<int:pk>/devices/', views.devices_table_view,
         name='devices'),
    path('device/<int:pk>/', views.device_detail_view, name='device'),
]
