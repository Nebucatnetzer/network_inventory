from django.test import Client

import pytest
from mixer.backend.django import mixer

from core.tests import helper
from devices.models import DeviceCategory


pytestmark = pytest.mark.django_db


def test_load_device_category_create_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get('/create/devices/category/')
    assert response.status_code == 200


def test_device_category_create_view(create_admin_user):
    user = create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend('computers.Computer', customer=user['customer'])
    session = client.session
    session['device_to_update'] = computer.pk
    session.save()
    data = {
        "name": "Foo",
        "save_category": "adf",
    }
    response = client.post('/create/devices/category/', data)
    assert (response.status_code == 200
            and helper.in_content(response, 'Foo'))


def test_device_category_create_view_invalid_form(create_admin_user):
    user = create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend('computers.Computer', customer=user['customer'])
    session = client.session
    session['device_to_update'] = computer.pk
    session.save()
    data = {
        "name": " ",
        "save_category": "adf",
    }
    response = client.post('/create/devices/category/', data)
    assert (response.status_code == 200
            and helper.in_content(response, 'This field is required.'))
