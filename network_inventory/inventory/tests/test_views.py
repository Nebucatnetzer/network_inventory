import pytest
from mixer.backend.django import mixer

from django.urls import resolve
from django.test import Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from inventory.models import (Backup, Device, Customer, Computer, Net,
                              Ram,  ComputerRamRelation,
                              RaidType, RaidInComputer, DisksInRaid, Disk,
                              Cpu, ComputerCpuRelation)

from helper import in_content, not_in_content

pytestmark=pytest.mark.django_db


def test_customer_list_view_not_logged_in():
    response = Client().get('/')
    assert response.status_code == 302 and 'login' in response.url


def test_customer_list_view_no_customer():
    User = get_user_model()
    admin = User.objects.create_user("novartis-admin", "admin@novartis.com",
                                     "password", is_staff=True)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/')
    assert response.status_code == 200


def test_customer_list_view(create_admin_user):
    fixture = create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/')
    assert (response.status_code == 200
            and in_content(response, fixture['customer'].name))


def test_customer_detail_view_not_logged_in():
    mixer.blend('inventory.Customer')
    response = Client().get('/customer/1/')
    assert response.status_code == 302 and 'login' in response.url


def test_customer_detail_view_not_found(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/customer/2/')
    assert response.status_code == 404


def test_customer_detail_view(create_admin_user):
    fixture = create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/customer/1/')
    assert (response.status_code == 200
            and in_content(response, fixture['customer'].name))


def test_customer_detail_view_no_permissions():
    User = get_user_model()
    admin = User.objects.create_user("novartis-admin", "admin@novartis.com",
                                     "password", is_staff=True)
    client = Client()
    customer = mixer.blend('inventory.Customer')
    client.login(username="novartis-admin", password="password")
    response = client.get('/customer/1/')
    assert response.status_code == 302 and 'login' in response.url


def test_customer_computer_table_not_logged_in():
    response = Client().get('/customer/1/computers/')
    assert response.status_code == 302 and 'login' in response.url


def test_customer_computer_table(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    computer = mixer.blend('inventory.Computer', customer=mixer.SELECT)
    response = client.get('/customer/1/computers/')
    assert response.status_code == 200 and in_content(response, computer.name)


def test_customer_computer_table_no_computer(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/customer/1/computers/')
    assert response.status_code == 200 and not_in_content(response, "Novartis PC")


def test_customer_device_table_not_logged_in():
    response = Client().get('/customer/1/devices/')
    assert response.status_code == 302 and 'login' in response.url


def test_computer_detail_view_not_logged_in():
    customer = mixer.blend('inventory.Customer')
    computer = mixer.blend('inventory.Computer', customer=customer)
    response = Client().get('/computer/1/')
    assert response.status_code == 302 and 'login' in response.url


def test_computer_detail_view(create_admin_user):
    create_admin_user()
    computer = mixer.blend('inventory.Computer', customer=mixer.SELECT)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/1/')
    assert response.status_code == 200 and in_content(response, computer.name)


def test_computer_detail_view_not_found(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/100/')
    assert response.status_code == 404


def test_computer_detail_view_ram_relation(create_admin_user):
    create_admin_user()
    computer = mixer.blend('inventory.Computer', customer=mixer.SELECT)
    ram_type = mixer.blend('inventory.RamType')
    ram = mixer.blend('inventory.Ram', ram_type=ram_type)
    mixer.blend('inventory.ComputerRamRelation', computer=computer, ram=ram)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/1/')
    assert response.status_code == 200 and in_content(response, "RAM Modules:")


def test_computer_detail_view_raid_relation(create_admin_user):
    create_admin_user()
    computer = mixer.blend('inventory.Computer', customer=mixer.SELECT)
    raid = mixer.blend('inventory.RaidType')
    disk = mixer.blend('inventory.Disk')
    disks = mixer.blend('inventory.DisksInRaid', raid=raid, disk=disk)
    mixer.blend('inventory.RaidInComputer', computer=computer, raid=disks)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/1/')
    assert response.status_code == 200 and in_content(response, "RAID")


def test_computer_detail_view_cpu_relation(create_admin_user):
    create_admin_user()
    computer = mixer.blend('inventory.Computer', customer=mixer.SELECT)
    cpu = mixer.blend('inventory.Cpu', cpu_typ=mixer.SELECT)
    mixer.blend('inventory.ComputerCpuRelation', cpu=cpu, computer=computer)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/1/')
    assert response.status_code == 200 and in_content(response, cpu.name)


def test_device_detail_view_not_logged_in():
    mixer.blend('inventory.Customer')
    mixer.blend('inventory.Device', customer=mixer.SELECT)
    response = Client().get('/device/1/')
    assert response.status_code == 302 and 'login' in response.url


def test_device_detail_view(create_admin_user):
    create_admin_user()
    device = mixer.blend('inventory.Device', customer=mixer.SELECT)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/device/1/')
    assert response.status_code == 200 and in_content(response, device.name)


def test_device_detail_view_not_found(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/device/100/')
    assert response.status_code == 404


def test_net_detail_view_not_logged_in():
    customer = Customer.objects.create(name="Novartis")
    Net.objects.create(name="Novartis Device", customer=customer)
    response = Client().get('/net/1/')
    assert response.status_code == 302 and 'login' in response.url


def test_net_detail_view(create_admin_user):
    create_admin_user()
    net = mixer.blend('inventory.Net')
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/net/1/')
    assert response.status_code == 200 and in_content(response, net.name)


def test_net_detail_view_not_found(create_admin_user):
    create_admin_user()
    net = mixer.blend('inventory.Net')
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/net/100/')
    assert response.status_code == 200 and not_in_content(response, net.name)


def test_backup_detail_view_not_logged_in():
    customer = Customer.objects.create(name="Novartis")
    computer = Computer.objects.create(name="Novartis PC")
    Backup.objects.create(name="Novartis Backup", computer=computer,
                          exec_time="21:30")
    response = Client().get('/backup/1/')
    assert response.status_code == 302 and 'login' in response.url


def test_backup_detail_view(create_admin_user):
    create_admin_user()
    computer = mixer.blend('inventory.Computer')
    backup = mixer.blend('inventory.Backup', computer=computer)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/backup/1/')
    assert response.status_code == 200 and in_content(response, backup.name)


def test_backup_detail_view_not_found(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/backup/100/')
    assert response.status_code == 200


def test_computer_list_view_not_logged_in():
    response = Client().get('/computers/all/')
    assert response.status_code == 302 and 'login' in response.url


def test_computer_list_view_no_computers(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computers/all/')
    assert response.status_code == 200


def test_computer_list_view(create_admin_user):
    fixture = create_admin_user()
    computer = mixer.blend('inventory.Computer',
                           customer=fixture['customer'])
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computers/all/')
    assert response.status_code == 200 and in_content(response, computer.name)
