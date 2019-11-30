import pytest
from mixer.backend.django import mixer

from django.test import Client
from django.contrib.auth import get_user_model

from inventory.models import DeviceInNet

import helper

pytestmark = pytest.mark.django_db


def test_net_detail_view_no_permission(create_admin_user):
    create_admin_user()
    net = mixer.blend('inventory.Net')
    device = mixer.blend('inventory.Computer')
    device_in_net = DeviceInNet.objects.create(device=device, net=net, ip='10.7.89.101')
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/net/' + str(net.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, net.name)
            and helper.not_in_content(response, device_in_net.ip))


def test_net_detail_view(create_admin_user):
    fixture = create_admin_user()
    net = mixer.blend('inventory.Net')
    device = mixer.blend('inventory.Computer', customer=fixture['customer'])
    device_in_net = DeviceInNet.objects.create(device=device,
                                               net=net, ip='10.7.89.101')
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/net/' + str(net.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, net.name)
            and helper.in_content(response, device_in_net.ip))


def test_net_detail_view_not_found(create_admin_user):
    create_admin_user()
    mixer.blend('inventory.Net')
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/net/100/')
    assert response.status_code == 404
