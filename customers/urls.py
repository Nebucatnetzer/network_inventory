from django.urls import path

from . import views

urlpatterns = [
    path('', views.customers_table_view, name='customers'),
    path('customer/<int:pk>/', views.CustomerDetailView.as_view(),
         name='customer'),
    path('create/customer/',
         views.CustomerCreateView.as_view(),
         name='customer_create'),
]
