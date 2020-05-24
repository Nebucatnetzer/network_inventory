from django.test import RequestFactory
from mixer.backend.django import mixer

import pytest

from devices import views


pytestmark = pytest.mark.django_db


def test_device_create_view(create_admin_user):
    fixture = create_admin_user()
    data = {'name': 'Test Device',
            'customer': fixture['customer'].id}
    request = RequestFactory().post('/', data=data)
    request.user = fixture['admin']
    response = views.DeviceCreateFromCustomerView.as_view()(
        request, pk=fixture['customer'].id)
    assert response.status_code == 302


def test_device_delete_view(create_admin_user):
    fixture = create_admin_user()
    device = mixer.blend('devices.Device')
    request = RequestFactory().post('/')
    request.user = fixture['admin']
    response = views.DeviceDeleteView.as_view()(request, pk=device.pk)
    assert response.status_code == 302


def test_device_update_view(create_admin_user):
    fixture = create_admin_user()
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
    request = RequestFactory().post('/', data=data)
    request.user = fixture['admin']
    response = views.DeviceUpdateView.as_view()(request, pk=device.pk)
    assert response.status_code == 302
    device.refresh_from_db()
    assert device.name == data['name']


def test_warranty_create_view(create_admin_user):
    fixture = create_admin_user()
    device = mixer.blend('devices.Device', customer=mixer.SELECT)
    data = {
        'customer': device.customer.id,
        'device': device.id,
        'valid_from': '2020-05-24',
        'valid_until': '2020-05-25',
        'warranty_type': ''
    }
    request = RequestFactory().post('/', data=data)
    request.user = fixture['admin']
    response = views.WarrantyCreateView.as_view()(
        request,
        pk=fixture['customer'].id)
    assert response.status_code == 302


