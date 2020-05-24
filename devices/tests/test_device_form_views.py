from django.http import Http404
from django.shortcuts import get_object_or_404
from django.test import RequestFactory
from mixer.backend.django import mixer

import pytest

from devices import models
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
    with pytest.raises(Http404):
        get_object_or_404(models.Device, pk=device.pk)
