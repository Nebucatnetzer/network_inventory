from django.urls import path

from . import views

urlpatterns = [
    path('', views.customers_table_view, name='customers'),
    path('customer/<int:pk>/', views.CustomerDetailView.as_view(),
         name='customer'),
    path('customer/<int:customer_id>/computers',
         views.computers_table_view, name='computers'),
    path('device/<int:device_id>/', views.device_detail_view, name='device'),
    path('computer/<int:computer_id>/', views.computer_detail_view,
         name='computer'),
    path('customer/<int:customer_id>/devices/', views.devices_table_view,
         name='devices'),
    path('customer/<int:customer_id>/nets/', views.nets_table_view,
         name='nets'),
    path('net/<int:pk>/', views.net_detail_view, name='net'),
 ]
