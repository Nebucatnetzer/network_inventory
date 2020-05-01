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
    path('customer/<int:pk>/create/device/',
         views.DeviceCreateFromCustomerView.as_view(),
         name='device_create'),
    path('update/device/<int:pk>/',
         views.DeviceUpdateView.as_view(),
         name='device_update'),
    path('device/<int:pk>/add/warranty/', views.WarrantyCreateView.as_view(),
         name='warranty_create'),
    path('warranties/', views.warranties_view, name='warranties'),
]
