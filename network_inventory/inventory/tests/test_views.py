import pytest
from mixer.backend.django import mixer

from django.urls import resolve
from django.test import Client
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from inventory.models import Backup, Device, Customer, Computer, Net

pytestmark=pytest.mark.django_db


def test_customer_list_view_not_logged_in():
    client = Client().get('/')
    assert client.status_code == 302


def test_customer_list_view_no_customer(create_admin_user):
    User = get_user_model()
    admin = User.objects.create_user("novartis-admin", "admin@novartis.com",
                                     "password", is_staff=True)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/')
    assert (response.status_code == 200
            and "Novartis" not in response.content.decode('utf8'))


def test_customer_list_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/')
    assert (response.status_code == 200
            and "Novartis" in response.content.decode('utf8'))


def test_customer_detail_view_not_logged_in():
    mixer.blend('inventory.Customer')
    client = Client().get('/customer/1/')
    assert client.status_code == 302


def test_customer_detail_view_not_found(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/customer/2/')
    assert response.status_code == 404


def test_customer_detail_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/customer/1/')
    assert response.status_code == 200


def test_customer_detail_view_no_permissions():
    User = get_user_model()
    admin = User.objects.create_user("novartis-admin", "admin@novartis.com",
                                     "password", is_staff=True)
    client = Client()
    Customer.objects.create(name="Novartis")
    client.login(username="novartis-admin", password="password")
    response = client.get('/customer/1/')
    assert "Novartis" not in response.content.decode('utf8')


def test_customer_computer_table_not_logged_in():
    client = Client().get('/customer/1/computers/')
    assert client.status_code == 302


def test_customer_computer_table(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/customer/1/computers/')
    assert False, "To be done"


def test_customer_computer_table_no_computer(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/customer/1/computers/')
    assert False, "To be done"


def test_customer_device_table_not_logged_in():
    client = Client().get('/customer/1/devices/')
    assert client.status_code == 302


def test_computer_detail_view_not_logged_in():
    customer = mixer.blend('inventory.Customer')
    computer = mixer.blend('inventory.Computer', customer=customer)
    client = Client().get('/computer/1/')
    assert client.status_code == 302


def test_computer_detail_view(create_admin_user):
    fixture = create_admin_user()
    computer = mixer.blend('inventory.Computer', customer=fixture['customer'])
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/1/')
    assert response.status_code == 200


def test_computer_detail_view_not_found(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/100/')
    assert response.status_code == 404

def test_computer_detail_view_ram_relation(create_admin_user):
    fixture = create_admin_user()
    Computer.objects.create(name="Novartis PC", customer=fixture['customer'])
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/1/')
    assert False, "To be done"


def test_computer_detail_view_raid_relation(create_admin_user):
    fixture = create_admin_user()
    Computer.objects.create(name="Novartis PC", customer=fixture['customer'])
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/1/')
    assert False, "To be done"


def test_computer_detail_view_cpu_relation(create_admin_user):
    fixture = create_admin_user()
    Computer.objects.create(name="Novartis PC", customer=fixture['customer'])
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/1/')
    assert False, "To be done"


def test_device_detail_view_not_logged_in():
    customer = Customer.objects.create(name="Novartis")
    Device.objects.create(name="Novartis Device", customer=customer)
    client = Client().get('/device/1/')
    assert client.status_code == 302


def test_device_detail_view(create_admin_user):
    fixture = create_admin_user()
    Device.objects.create(name="Novartis Device", customer=fixture['customer'])
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/device/1/')
    assert response.status_code == 200


def test_device_detail_view_not_found(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/device/100/')
    assert response.status_code == 404


def test_net_detail_view_not_logged_in():
    customer = Customer.objects.create(name="Novartis")
    Net.objects.create(name="Novartis Device", customer=customer)
    client = Client().get('/net/1/')
    assert client.status_code == 302


def test_net_detail_view(create_admin_user):
    fixture = create_admin_user()
    Net.objects.create(name="Novartis Device", customer=fixture['customer'])
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/net/1/')
    assert False, "To be done"


def test_net_detail_view_not_found(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/net/100/')
    assert False, "To be done"


def test_backup_detail_view_not_logged_in():
    customer = Customer.objects.create(name="Novartis")
    computer = Computer.objects.create(name="Novartis PC")
    Backup.objects.create(name="Novartis Backup", computer=computer,
                          exec_time="21:30")
    client = Client().get('/backup/1/')
    assert client.status_code == 302


def test_backup_detail_view(create_admin_user):
    fixture = create_admin_user()
    computer = Computer.objects.create(name="Novartis PC")
    Backup.objects.create(name="Novartis Backup", computer=computer,
                          exec_time="21:30")
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/backup/1/')
    assert False, "To be done"


def test_backup_detail_view_not_found(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/backup/100/')
    assert False, "To be done"


def test_computer_list_view_not_logged_in():
    client = Client().get('/computers/all/')
    assert client.status_code == 302


def test_computer_list_view_no_computers():
    client = Client().get('/computers/all/')
    assert False, "To be done"


def test_computer_list_view():
    client = Client().get('/computers/all/')
    assert False, "To be done"
