from django.urls import path

from . import views

urlpatterns = [
    path('', views.CustomerList.as_view(), name='customers'),
    path('customer/<int:pk>/', views.CustomerDetailView.as_view(),
         name='customer'),
         name='computers'),
    path('device/<int:device_id>/', views.device_details, name='device'),
    path('computer/<int:computer_id>/', views.computer_details,
         name='computer'),
    path('devices/<int:customer_id>', views.DeviceList.as_view(),
         name='devices'),
    path('customer/<int:customer_id>/lists/', views.list_of_lists,
         name='lists'),
 ]
