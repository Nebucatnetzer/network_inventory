import pytest
from mixer.backend.django import mixer

from django.test import Client

import helper

pytestmark = pytest.mark.django_db


def test_device_detail_view_not_logged_in():
    response = Client().get('/device/1/')
    assert response.status_code == 302 and 'login' in response.url


def test_device_detail_view(create_admin_user):
    create_admin_user()
    mixer.blend('inventory.DeviceCategory')
    mixer.blend('inventory.Owner')
    mixer.blend('inventory.Location')
    device = mixer.blend('inventory.Device', customer=mixer.SELECT,
                         owner=mixer.SELECT, category=mixer.SELECT,
                         manufacturer=mixer.SELECT,
                         location=mixer.SELECT)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/device/' + str(device.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, str(device))
            and helper.in_content(response, str(device.serialnumber))
            and helper.in_content(response, str(device.category))
            and helper.in_content(response, str(device.owner))
            and helper.in_content(response, str(device.customer))
            and helper.in_content(response, str(device.manufacturer))
            and helper.in_content(response, str(device.location)))


def test_device_detail_view_not_found(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/device/100/')
    assert response.status_code == 404


def test_device_detail_view_no_permission(create_admin_user):
    create_admin_user()
    customer = mixer.blend('inventory.Customer')
    device = mixer.blend('inventory.Device', customer=customer)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/device/' + str(device.id) + '/')
    assert response.status_code == 403

