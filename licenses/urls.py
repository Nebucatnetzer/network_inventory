from django.urls import path

from . import views

urlpatterns = [
    path('customer/<int:pk>/licenses/', views.licenses_table_view,
         name='licenses'),
    path('create/license-with/computer/<int:pk>/',
         views.LicenseWithComputerCreateView.as_view(),
         name='license_with_computer_create'),
    path('delete/license-with-computer/<int:pk>/',
         views.LicenseWithComputerDeleteView.as_view(),
         name='license_with_computer_delete'),
 ]
