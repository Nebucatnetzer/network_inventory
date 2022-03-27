from django.urls import path

from . import views


urlpatterns = [
    path(
        "customer/<int:pk>/devices/", views.devices_table_view, name="devices"
    ),
    path("device/<int:pk>/", views.device_detail_view, name="device"),
    path(
        "manufacturer/<int:pk>/",
        views.DeviceManufacturerDetailView.as_view(),
        name="manufacturer",
    ),
    path(
        "customer/<int:pk>/create/device/",
        views.DeviceCreateFromCustomerView.as_view(),
        name="device_create",
    ),
    path(
        "update/device/<int:pk>/",
        views.device_update_view,
        name="device_update",
    ),
    path(
        "delete/device/<int:pk>/",
        views.DeviceDeleteView.as_view(),
        name="device_delete",
    ),
    path(
        "device/<int:pk>/add/warranty/",
        views.WarrantyCreateView.as_view(),
        name="warranty_create",
    ),
    path(
        "update/warranty/<int:pk>/",
        views.WarrantyUpdateView.as_view(),
        name="warranty_update",
    ),
    path(
        "delete/warranty/<int:pk>/",
        views.WarrantyDeleteView.as_view(),
        name="warranty_delete",
    ),
    path(
        "device/<int:pk>/add/device-in-net/",
        views.DeviceInNetCreateView.as_view(),
        name="device_in_net_create",
    ),
    path(
        "update/device-in-net/<int:pk>/",
        views.DeviceInNetUpdateView.as_view(),
        name="device_in_net_update",
    ),
    path(
        "delete/device-in-net/<int:pk>/",
        views.DeviceInNetDeleteView.as_view(),
        name="device_in_net_delete",
    ),
    path("warranties/", views.warranties_view, name="warranties"),
    path(
        "create/devices/category/",
        views.htmx_create_device_cagetory,
        name="device_category_create",
    ),
]
