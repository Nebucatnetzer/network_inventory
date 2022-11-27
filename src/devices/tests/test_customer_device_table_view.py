import pytest

from django.test import Client
from mixer.backend.django import mixer

from core.tests import helper
from customers.models import Customer

pytestmark = pytest.mark.django_db


def test_customer_device_table_not_logged_in():
    response = Client().get("/customer/1/devices/")
    assert response.status_code == 302 and "login" in response.url


def test_customer_device_table(create_admin_user):
    fixture = create_admin_user()
    customer = fixture["customer"]
    client = Client()
    client.login(username="pharma-admin", password="password")
    device = mixer.blend("devices.Device", customer=mixer.SELECT)
    response = client.get("/customer/" + str(customer.id) + "/devices/")
    assert response.status_code == 200 and helper.in_content(response, device)


def test_customer_device_table_no_device(create_admin_user):
    fixture = create_admin_user()
    customer = fixture["customer"]
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get("/customer/" + str(customer.id) + "/devices/")
    assert response.status_code == 200 and helper.not_in_content(
        response, "Pharma Corp. PC"
    )


def test_customer_device_table_no_permission(create_admin_user):
    create_admin_user()
    customer = Customer.objects.create(name="Water Corp.")
    client = Client()
    client.login(username="pharma-admin", password="password")
    mixer.blend("devices.Device", customer=customer)
    response = client.get("/customer/" + str(customer.id) + "/devices/")
    assert response.status_code == 403


def test_customer_device_table_multiple_devices(create_admin_user):
    fixture = create_admin_user()
    customer = fixture["customer"]
    client = Client()
    client.login(username="pharma-admin", password="password")
    device1 = mixer.blend("devices.Device", customer=mixer.SELECT)
    device2 = mixer.blend("devices.Device", customer=mixer.SELECT)
    response = client.get("/customer/" + str(customer.id) + "/devices/")
    assert (
        response.status_code == 200
        and helper.in_content(response, device1)
        and helper.in_content(response, device2)
    )
