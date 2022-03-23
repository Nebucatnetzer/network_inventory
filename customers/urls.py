from django.urls import path

from . import views

urlpatterns = [
    path('', views.customers_table_view, name='customers'),
    path('customer/<int:pk>/', views.customer_detail_view,
         name='customer'),
    path('delete/customer/<int:pk>/', views.CustomerDeleteView.as_view(),
         name='customer_delete'),
    path('create/customer/',
         views.create_customer,
         name='customer_create'),
    path('create/location/', views.htmx_create_location,
         name='htmx_create_location')
]
