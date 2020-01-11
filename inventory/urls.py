from django.urls import path, include

from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('customer/<int:pk>/computers/',
         views.computers_table_view, name='computers'),
    path('computer/<int:pk>/', views.computer_detail_view,
         name='computer'),
    path('computers/all/', views.ComputersFilterView.as_view(),
         name='all_computers'),
    path('customer/<int:pk>/licenses/', views.licenses_table_view,
         name='licenses'),
 ]
