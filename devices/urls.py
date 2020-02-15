from django.urls import path

from . import views


urlpatterns = [
    path('connected_device/<int:pk>/', views.connected_device_detail_view,
         name='connected_device'),
    path('customer/<int:pk>/devices/', views.devices_table_view,
         name='devices'),
    path('customer/<int:pk>/connected_devices/',
         views.connected_devices_table_view,
         name='connected_devices'),
    path('device/<int:pk>/', views.device_detail_view, name='device'),
]
