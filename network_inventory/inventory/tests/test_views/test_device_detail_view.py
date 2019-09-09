import pytest
from mixer.backend.django import mixer

from django.test import Client

from helper import in_content, not_in_content

pytestmark=pytest.mark.django_db


def test_device_detail_view_not_logged_in():
    response = Client().get('/device/1/')
    assert response.status_code == 302 and 'login' in response.url


def test_device_detail_view(create_admin_user):
    create_admin_user()
    device = mixer.blend('inventory.Device', customer=mixer.SELECT)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/device/' + str(device.id) + '/')
    assert response.status_code == 200 and in_content(response, device.name)


def test_device_detail_view_not_found(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/device/100/')
    assert response.status_code == 404
