from django.urls import path, include

from . import views

urlpatterns = [
    path('customer/<int:pk>/backups/', views.backups_table_view,
         name='backups'),
    path('backup/<int:pk>/', views.backup_detail_view, name='backup'),
 ]
