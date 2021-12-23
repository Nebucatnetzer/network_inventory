from django.urls import path

from . import views

urlpatterns = [
    path('', views.customers_table_view, name='customers'),
    path('customer/<int:pk>/', views.customer_detail_view,
         name='customer'),
    path('create/customer/',
         views.customer_create_view,
         name='customer_create'),
    path('delete/customer/<int:pk>/', views.CustomerDeleteView.as_view(),
         name='customer_delete'),
    path('htmx/create/customer/',
         views.htmx_create_customer,
         name='htmx_create_customer'),
]
