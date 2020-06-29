from django.urls import path

from . import views

urlpatterns = [
    path('customer/<int:pk>/backups/', views.backups_table_view,
         name='backups'),
    path('backup/<int:pk>/', views.backup_detail_view, name='backup'),
    path('create/backup-for-computer/<int:pk>/',
         views.BackupCreateView.as_view(), name='backup_create'),
    path('delete/backup/<int:pk>/',
         views.BackupDeleteView.as_view(), name='backup_delete'),
 ]
