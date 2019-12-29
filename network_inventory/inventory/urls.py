from django.urls import path, include

from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.customers_table_view, name='customers'),
    path('customer/<int:pk>/', views.CustomerDetailView.as_view(),
         name='customer'),
    path('customer/<int:pk>/computers/',
         views.computers_table_view, name='computers'),
    path('customer/<int:pk>/devices/', views.devices_table_view,
         name='devices'),
    path('customer/<int:pk>/nets/', views.nets_table_view,
         name='nets'),
    path('customer/<int:pk>/backups/', views.backups_table_view,
         name='backups'),
    path('computer/<int:pk>/', views.computer_detail_view,
         name='computer'),
    path('device/<int:pk>/', views.device_detail_view, name='device'),
    path('net/<int:pk>/', views.net_detail_view, name='net'),
    path('backup/<int:pk>/', views.backup_detail_view, name='backup'),
    path('computers/all/', views.ComputersFilterView.as_view(),
         name='all_computers'),
    path('customer/<int:pk>/licenses/', views.licenses_table_view,
         name='licenses'),
 ]
