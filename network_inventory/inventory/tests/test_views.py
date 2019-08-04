import pytest

from django.urls import resolve
from django.test import Client
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from inventory.models import Device, Customer, Computer


@pytest.mark.django_db
def test_customer_list_view_not_logged_in():
    client = Client().get('/')
    assert client.status_code == 302


@pytest.mark.django_db
def test_customer_list_view(create_admin_user):
    fixture = create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_customer_detail_view_not_logged_in():
    customer = Customer(name='Novartis')
    customer.save()
    client = Client().get('/customer/1/')
    assert client.status_code == 302


@pytest.mark.django_db
def test_customer_detail_view_not_found(create_admin_user):
    fixture = create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/customer/2/')
    assert response.status_code == 404


@pytest.mark.django_db
def test_customer_detail_view(create_admin_user):
    fixture = create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/customer/1/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_customer_computer_table_not_logged_in():
    client = Client().get('/customer/1/computers/')
    assert client.status_code == 302


@pytest.mark.django_db
def test_customer_computer_table(create_admin_user):
    fixture = create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/customer/1/computers/')
    print(response.content)
    assert response.status_code == 200


@pytest.mark.django_db
def test_customer_device_table_not_logged_in():
    client = Client().get('/customer/1/devices/')
    assert client.status_code == 302


@pytest.mark.django_db
def test_computer_detail_view_not_logged_in():
    customer = Customer(name="Novartis")
    customer.save()
    computer = Computer(name="Novartis PC", customer=customer)
    computer.save()
    client = Client().get('/computer/1/')
    assert client.status_code == 302


@pytest.mark.django_db
def test_computer_detail_view(create_admin_user):
    fixture = create_admin_user()
    computer = Computer(name="Novartis PC", customer=fixture['customer'])
    computer.save()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/1/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_device_detail_view():
    device = Device(name='Novartis Device')
    device.save()
    client = Client().get('/device/1/')
    assert client.status_code == 302


@pytest.mark.django_db
def test_device_detail_view_not_found():
    client = Client().get('/device/1/')
    assert client.status_code == 302


@pytest.mark.django_db
def test_computer_list_view():
    client = Client().get('/computers/all/')
    assert client.status_code == 302
