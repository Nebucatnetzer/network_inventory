from django.urls import path

from . import views

urlpatterns = [
    path(
        "customer/<int:pk>/computers/",
        views.computers_table_view,
        name="computers",
    ),
    path("computer/<int:pk>/", views.computer_detail_view, name="computer"),
    path(
        "computers/all/",
        views.ComputersFilterView.as_view(),
        name="all_computers",
    ),
    path(
        "customer/<int:pk>/create/computer/",
        views.ComputerCreateFromCustomerView.as_view(),
        name="computer_create",
    ),
    path(
        "update/computer/<int:pk>/",
        views.computer_update_view,
        name="computer_update",
    ),
    path(
        "delete/computer/<int:pk>/",
        views.ComputerDeleteView.as_view(),
        name="computer_delete",
    ),
    path(
        "computer/<int:pk>/create/ram-relation/",
        views.ComputerRamRelationCreateView.as_view(),
        name="ram_relation_create",
    ),
    path(
        "delete/ram-relation/<int:pk>/",
        views.ComputerRamRelationDeleteView.as_view(),
        name="ram_relation_delete",
    ),
    path(
        "computer/<int:pk>/create/cpu-relation/",
        views.ComputerCpuRelationCreateView.as_view(),
        name="cpu_relation_create",
    ),
    path(
        "delete/cpu-relation/<int:pk>/",
        views.ComputerCpuRelationDeleteView.as_view(),
        name="cpu_relation_delete",
    ),
    path(
        "computer/<int:pk>/create/gpu-relation/",
        views.ComputerGpuRelationCreateView.as_view(),
        name="gpu_relation_create",
    ),
    path(
        "delete/gpu-relation/<int:pk>/",
        views.ComputerGpuRelationDeleteView.as_view(),
        name="gpu_relation_delete",
    ),
    path(
        "computer/<int:pk>/create/disk-relation/",
        views.ComputerDiskRelationCreateView.as_view(),
        name="disk_relation_create",
    ),
    path(
        "delete/disk-relation/<int:pk>/",
        views.ComputerDiskRelationDeleteView.as_view(),
        name="disk_relation_delete",
    ),
    path(
        "computer/<int:pk>/create/software-relation/",
        views.ComputerSoftwareRelationCreateView.as_view(),
        name="software_relation_create",
    ),
    path(
        "delete/software-relation/<int:pk>/",
        views.ComputerSoftwareRelationDeleteView.as_view(),
        name="software_relation_delete",
    ),
    path(
        "computer/<int:pk>/create/raid/",
        views.RaidCreateView.as_view(),
        name="raid_create",
    ),
    path(
        "delete/raid/<int:pk>/",
        views.RaidDeleteView.as_view(),
        name="raid_delete",
    ),
]
