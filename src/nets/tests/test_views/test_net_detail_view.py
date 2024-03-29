import pytest
from mixer.backend.django import mixer

from django.test import Client

from devices.models import DeviceInNet

from core.tests import helper

pytestmark = pytest.mark.django_db


def test_net_detail_view_no_permission(create_admin_user):
    create_admin_user()
    net = mixer.blend("nets.Net")
    customer = mixer.blend("customers.Customer")
    device = mixer.blend("computers.Computer", customer=customer)
    mixer.blend("devices.DeviceInNet", device=device, net=net, ip="10.7.89.101")
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get("/net/" + str(net.id) + "/")
    assert response.status_code == 403


def test_net_detail_view(create_admin_user):
    fixture = create_admin_user()
    net = mixer.blend("nets.Net", customer=mixer.SELECT)
    device = mixer.blend("computers.Computer", customer=fixture["customer"])
    device_in_net = DeviceInNet.objects.create(device=device, net=net, ip="10.7.89.101")
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get("/net/" + str(net.id) + "/")
    assert (
        response.status_code == 200
        and helper.in_content(response, net)
        and helper.in_content(response, device_in_net.ip)
    )


def test_net_detail_view_not_found(create_admin_user):
    create_admin_user()
    mixer.blend("nets.Net")
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get("/net/100/")
    assert response.status_code == 404
