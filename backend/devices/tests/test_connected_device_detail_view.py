import pytest
from mixer.backend.django import mixer

from django.test import Client

from core.tests import helper
from nets.models import IpStatus

pytestmark = pytest.mark.django_db


def test_device_detail_view_net_relation(create_admin_user):
    create_admin_user()
    device = mixer.blend('devices.Device', customer=mixer.SELECT)
    net1 = mixer.blend('nets.Net', customer=mixer.SELECT)
    net2 = mixer.blend('nets.Net', customer=mixer.SELECT)
    device_in_net1 = mixer.blend('devices.DeviceInNet',
                                 device=device,
                                 net=net1,
                                 ip="10.7.89.100")
    device_in_net2 = mixer.blend('devices.DeviceInNet',
                                 device=device,
                                 net=net2,
                                 ip="10.8.89.100")
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get('/device/' + str(device.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, device_in_net1.ip)
            and helper.in_content(response, device_in_net2.ip))


def test_device_detail_view_net_dhcp_relation(create_admin_user):
    create_admin_user()
    device = mixer.blend('devices.Device', customer=mixer.SELECT)
    net1 = mixer.blend('nets.Net', customer=mixer.SELECT)
    ip_status = IpStatus.objects.filter(name="Dynamic")
    device_in_net1 = mixer.blend('devices.DeviceInNet',
                                 device=device,
                                 net=net1,
                                 ip_status=ip_status[0],
                                 ip="")
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get('/device/' + str(device.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, device_in_net1.ip_status))
