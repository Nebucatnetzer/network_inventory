import pytest
from mixer.backend.django import mixer

from django.test import Client

from core.tests import helper

pytestmark = pytest.mark.django_db


def test_device_detail_view_not_logged_in():
    response = Client().get('/device/1/')
    assert response.status_code == 302 and 'login' in response.url


def test_device_detail_view(create_admin_user):
    fixture = create_admin_user()
    mixer.blend('devices.DeviceCategory')
    mixer.blend('devices.HardwareModel')
    mixer.blend('customers.Owner')
    mixer.blend('customers.Location')
    device = mixer.blend('devices.Device',
                         customer=fixture['customer'],
                         owner=mixer.SELECT,
                         category=mixer.SELECT,
                         manufacturer=mixer.SELECT,
                         hardware_model=mixer.SELECT,
                         location=mixer.SELECT)
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get('/device/' + str(device.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, device)
            and helper.in_content(response, device.serialnumber)
            and helper.in_content(response, device.category)
            and helper.in_content(response, device.owner)
            and helper.in_content(response, device.customer)
            and helper.in_content(response, device.manufacturer)
            and helper.in_content(response, device.hardware_model)
            and helper.in_content(response, device.location))


def test_device_detail_view_not_found(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get('/device/100/')
    assert response.status_code == 404


def test_device_detail_view_no_permission(create_admin_user):
    create_admin_user()
    customer = mixer.blend('customers.Customer')
    device = mixer.blend('devices.Device', customer=customer)
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get('/device/' + str(device.id) + '/')
    assert response.status_code == 403


def test_device_detail_view_warranty(create_admin_user):
    fixture = create_admin_user()
    device = mixer.blend('devices.Device', customer=fixture['customer'])
    warranty = mixer.blend('devices.Warranty',
                           device=device,
                           valid_from="2020-01-01",
                           valid_until="2020-12-31")
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get('/device/' + str(device.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, warranty.duration_in_years))
