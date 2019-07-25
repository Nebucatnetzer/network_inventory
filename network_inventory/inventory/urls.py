from django.urls import path

from . import views

urlpatterns = [
    path('', views.CustomerListView.as_view(), name='customers'),
    path('customer/<int:pk>/', views.CustomerDetailView.as_view(),
         name='customer'),
    path('customer/<int:customer_id>/computers', views.ComputerListView.as_view(),
         name='computers'),
    path('device/<int:device_id>/', views.device_detail_view, name='device'),
    path('computer/<int:computer_id>/', views.computer_detail_view,
         name='computer'),
    path('devices/<int:customer_id>', views.DeviceListView.as_view(),
         name='devices'),
    path('customer/<int:customer_id>/lists/', views.list_of_lists,
         name='lists'),
 ]
