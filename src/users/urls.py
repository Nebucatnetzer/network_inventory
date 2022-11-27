from django.urls import path

from . import views

urlpatterns = [
    path("customer/<int:pk>/groups/", views.groups_table_view, name="groups"),
    path("group/<int:pk>/", views.group_detail_view, name="group"),
    path(
        "delete/group/<int:pk>/",
        views.delete_group,
        name="group_delete",
    ),
    path("customer/<int:pk>/users/", views.users_table_view, name="users"),
    path("user/<int:pk>/", views.user_detail_view, name="user"),
    path(
        "delete/user/<int:pk>/",
        views.UserDeleteView.as_view(),
        name="user_delete",
    ),
]
