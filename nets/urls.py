from django.urls import path

from . import views

urlpatterns = [
    path("customer/<int:pk>/nets/", views.nets_table_view, name="nets"),
    path("net/<int:pk>/", views.net_detail_view, name="net"),
    path(
        "delete/net/<int:pk>/",
        views.NetDeleteView.as_view(),
        name="net_delete",
    ),
]
