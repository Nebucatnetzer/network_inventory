from django.urls import path

from . import views

urlpatterns = [
    path('customer/<int:pk>/computers/',
         views.computers_table_view, name='computers'),
    path('computer/<int:pk>/', views.computer_detail_view,
         name='computer'),
    path('computers/all/', views.ComputersFilterView.as_view(),
         name='all_computers'),
    path('customer/<int:pk>/create/computer/', views.ComputerCreateFromCustomerView.as_view(),
         name='computer_create'),
    path('update/computer/<int:pk>/', views.ComputerUpdateView.as_view(),
         name='computer_update'),
 ]
