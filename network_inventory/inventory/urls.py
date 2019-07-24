from django.urls import path

from . import views

urlpatterns = [
    path('', views.CustomerList.as_view(), name='customers'),
    path('customer/<int:customer_id>/', views.ComputerList.as_view(),
         name='computers'),
    path('device/<int:device_id>/', views.device_details, name='device'),
    path('computer/<int:computer_id>/', views.computer_details,
         name='computer'),
    path('devices/', views.DeviceList.as_view(), name='devices'),
 ]
