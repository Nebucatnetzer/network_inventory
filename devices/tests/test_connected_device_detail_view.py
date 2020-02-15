import pytest
from mixer.backend.django import mixer

from django.test import Client

from core.tests import helper

pytestmark = pytest.mark.django_db


def test_connected_device_detail_view_not_logged_in():
    response = Client().get('/connected_device/1/')
    assert response.status_code == 302 and 'login' in response.url


def test_connected_device_detail_view(create_admin_user):
    fixture = create_admin_user()
    mixer.blend('devices.DeviceCategory')
    mixer.blend('devices.HardwareModel')
    mixer.blend('customers.Owner')
    mixer.blend('customers.Location')
    connected_device = mixer.blend('devices.ConnectedDevice',
                                   customer=fixture['customer'],
                                   owner=mixer.SELECT,
                                   category=mixer.SELECT,
                                   manufacturer=mixer.SELECT,
                                   hardware_model=mixer.SELECT,
                                   location=mixer.SELECT)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/connected_device/'
                          + str(connected_device.id)
                          + '/')
    assert (response.status_code == 200
            and helper.in_content(response, connected_device)
            and helper.in_content(response, connected_device.serialnumber)
            and helper.in_content(response, connected_device.category)
            and helper.in_content(response, connected_device.owner)
            and helper.in_content(response, connected_device.customer)
            and helper.in_content(response, connected_device.manufacturer)
            and helper.in_content(response, connected_device.hardware_model)
            and helper.in_content(response, connected_device.location))


def test_connected_device_detail_view_not_found(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/connected_device/100/')
    assert response.status_code == 404


def test_connected_device_detail_view_no_permission(create_admin_user):
    create_admin_user()
    customer = mixer.blend('customers.Customer')
    connected_device = mixer.blend('devices.ConnectedDevice',
                                   customer=customer)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/connected_device/'
                          + str(connected_device.id)
                          + '/')
    assert response.status_code == 403


def test_connected_device_detail_view_net_relation(create_admin_user):
    create_admin_user()
    device = mixer.blend('devices.ConnectedDevice', customer=mixer.SELECT)
    net = mixer.blend('nets.Net', customer=mixer.SELECT)
    device_in_net = mixer.blend('devices.DeviceInNet',
                                device=device,
                                net=net,
                                ip="10.7.89.100")
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/connected_device/' + str(device.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, device_in_net.ip))
