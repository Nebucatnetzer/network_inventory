from django.urls import path

from . import views

urlpatterns = [
    path('customer/<int:pk>/groups/', views.groups_table_view,
         name='groups'),
    path('ad-group/<int:pk>/', views.ad_group_detail_view, name='ad_group'),
    path('mail-group/<int:pk>/', views.mail_group_detail_view,
         name='mail_group'),
    path('delete/ad-group/<int:pk>/', views.delete_ad_group,
         name='ad_group_delete'),
    path('delete/mail-group/<int:pk>/', views.delete_mail_group,
         name='mail_group_delete'),
    path('customer/<int:pk>/users/', views.users_table_view,
         name='users'),
    path('user/<int:pk>/', views.user_detail_view, name='user'),
    path('delete/user/<int:pk>/', views.UserDeleteView.as_view(),
         name='user_delete')
]
