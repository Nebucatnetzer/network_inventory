from datetime import datetime

from django.test import Client
from mixer.backend.django import mixer
import pytest

from core.tests import helper


pytestmark = pytest.mark.django_db


def test_device_create_view(create_admin_user):
    fixture = create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    data = {"name": "Test Device", "customer": fixture["customer"].id}
    url = "/customer/{}/create/device/".format(fixture["customer"].id)
    response = client.post(url, data)
    assert response.status_code == 302


def test_device_delete_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    device = mixer.blend("devices.Device")
    response = client.post("/delete/device/{}/".format(device.pk))
    assert response.status_code == 302


def test_load_device_update_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    device = mixer.blend("devices.Device", customer=mixer.SELECT)
    response = client.get("/update/device/{}/".format(device.pk))
    assert response.status_code == 200 and helper.in_content(response, device.name)


def test_device_update_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    device = mixer.blend("devices.Device", customer=mixer.SELECT)
    data = {
        "name": "Foo",
        "description": "",
        "serialnumber": "",
        "category": "",
        "owner": "",
        "customer": device.customer.id,
        "manufacturer": "",
        "model": "",
        "location": "",
        "user": "",
        "installation_date": "",
        "save_device": "",
    }
    response = client.post("/update/device/{}/".format(device.pk), data)
    assert response.status_code == 302
    device.refresh_from_db()
    assert device.name == data["name"]


def test_device_update_view_wrong_name(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    device1 = mixer.blend("devices.Device", customer=mixer.SELECT)
    device2 = mixer.blend("devices.Device", customer=mixer.SELECT)
    data = {
        "name": device2.name,
        "description": "",
        "serialnumber": "",
        "category": "",
        "owner": "",
        "customer": device1.customer.id,
        "manufacturer": "",
        "model": "",
        "location": "",
        "user": "",
        "installation_date": "",
        "save_device": "",
    }
    response = client.post("/update/device/{}/".format(device1.pk), data)
    assert response.status_code == 200 and helper.in_content(
        response, "Device with this Name and Customer already exists."
    )


def test_warranty_create_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    device = mixer.blend("devices.Device", customer=mixer.SELECT)
    data = {
        "customer": device.customer.id,
        "device": device.id,
        "valid_from": "2020-05-24",
        "valid_until": "2020-05-25",
        "warranty_type": "",
    }
    url = "/device/{}/add/warranty/".format(device.id)
    response = client.post(url, data)
    assert response.status_code == 302


def test_warranty_update_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    device = mixer.blend("devices.Device", customer=mixer.SELECT)
    warranty = mixer.blend(
        "devices.Warranty",
        customer=device.customer,
        device=device,
        valid_from="2019-05-24",
        valid_until="2020-05-25",
    )
    data = {
        "customer": device.customer.id,
        "device": device.id,
        "valid_from": "2020-05-24",
        "valid_until": "2020-05-25",
        "warranty_type": "",
    }
    response = client.post("/update/warranty/{}/".format(warranty.pk), data)
    date_from = datetime.strptime(data["valid_from"], "%Y-%m-%d").date()
    assert response.status_code == 302
    warranty.refresh_from_db()
    assert warranty.valid_from == date_from


def test_warranty_delete_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    device = mixer.blend("devices.Device", customer=mixer.SELECT)
    warranty = mixer.blend(
        "devices.Warranty",
        customer=device.customer,
        device=device,
        valid_from="2019-05-24",
        valid_until="2020-05-25",
    )
    url = "/delete/warranty/{}/".format(warranty.id)
    response = client.post(url)
    assert response.status_code == 302


def test_device_in_net_create_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    device = mixer.blend("devices.Device", customer=mixer.SELECT)
    net = mixer.blend("nets.Net", customer=device.customer)
    data = {
        "device": device.id,
        "net": net.id,
        "ip": "192.168.1.20",
        "nic": "",
        "mac_address": "",
        "ip_status": "1",
    }
    url = "/device/{}/add/device-in-net/".format(device.id)
    response = client.post(url, data)
    assert response.status_code == 302


def test_device_in_net_update_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    device = mixer.blend("devices.Device", customer=mixer.SELECT)
    net = mixer.blend("nets.Net", customer=device.customer)
    device_in_net = mixer.blend(
        "devices.DeviceInNet", customer=device.customer, device=device, net=net
    )
    data = {
        "device": device.id,
        "net": net.id,
        "ip": "192.168.1.20",
        "nic": "",
        "mac_address": "",
        "ip_status": "1",
    }
    response = client.post("/update/device-in-net/{}/".format(device_in_net.pk), data)
    assert response.status_code == 302
    device_in_net.refresh_from_db()
    assert device_in_net.ip == data["ip"]


def test_device_in_net_delete_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    device = mixer.blend("devices.Device", customer=mixer.SELECT)
    net = mixer.blend("nets.Net", customer=device.customer)
    device_in_net = mixer.blend(
        "devices.DeviceInNet", customer=device.customer, device=device, net=net
    )
    url = "/delete/device-in-net/{}/".format(device_in_net.id)
    response = client.post(url)
    assert response.status_code == 302
