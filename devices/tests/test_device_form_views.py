from datetime import datetime

from django.test import Client
from mixer.backend.django import mixer
import pytest


pytestmark = pytest.mark.django_db


def test_device_create_view(create_admin_user):
    fixture = create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    data = {'name': 'Test Device',
            'customer': fixture['customer'].id}
    url = '/customer/{}/create/device/'.format(fixture['customer'].id)
    response = client.post(url, data)
    assert response.status_code == 302


def test_device_delete_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    device = mixer.blend('devices.Device')
    response = client.post('/delete/device/{}/'.format(device.pk))
    assert response.status_code == 302


def test_device_update_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    device = mixer.blend('devices.Device', customer=mixer.SELECT)
    data = {'name': 'Foo',
            'description': '',
            'serialnumber': '',
            'category': '',
            'owner': '',
            'customer': device.customer.id,
            'manufacturer': '',
            'model': '',
            'location': '',
            'user': '',
            'installation_date': ''}
    response = client.post('/update/device/{}/'.format(device.pk), data)
    assert response.status_code == 302
    device.refresh_from_db()
    assert device.name == data['name']


def test_warranty_create_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    device = mixer.blend('devices.Device', customer=mixer.SELECT)
    data = {
        'customer': device.customer.id,
        'device': device.id,
        'valid_from': '2020-05-24',
        'valid_until': '2020-05-25',
        'warranty_type': ''
    }
    url = '/device/{}/add/warranty/'.format(device.id)
    response = client.post(url, data)
    assert response.status_code == 302


def test_warranty_update_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    device = mixer.blend('devices.Device', customer=mixer.SELECT)
    warranty = mixer.blend('devices.Warranty',
                           customer=device.customer,
                           device=device)
    data = {
        'customer': device.customer.id,
        'device': device.id,
        'valid_from': '2020-05-24',
        'valid_until': '2020-05-25',
        'warranty_type': ''
    }
    response = client.post('/update/warranty/{}/'.format(warranty.pk), data)
    date_from = datetime.strptime(data['valid_from'], "%Y-%m-%d").date()
    assert response.status_code == 302
    warranty.refresh_from_db()
    assert warranty.valid_from == date_from
