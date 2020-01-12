from django.urls import path

from . import views

urlpatterns = [
        path('customer/<int:pk>/licenses/', views.licenses_table_view,
             name='licenses'),
 ]
