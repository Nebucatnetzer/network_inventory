import pytest
from mixer.backend.django import mixer

from django.test import Client

import helper

pytestmark = pytest.mark.django_db


def test_computer_detail_view_not_logged_in():
    response = Client().get('/computer/1/')
    assert response.status_code == 302 and 'login' in response.url


def test_computer_detail_view(create_admin_user):
    create_admin_user()
    computer = mixer.blend('inventory.Computer', customer=mixer.SELECT)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/' + str(computer.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, computer.name))


def test_computer_detail_view_not_found(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/230/')
    assert response.status_code == 404


def test_computer_detail_view_ram_relation(create_admin_user):
    create_admin_user()
    computer = mixer.blend('inventory.Computer', customer=mixer.SELECT)
    ram_type = mixer.blend('inventory.RamType')
    ram = mixer.blend('inventory.Ram', ram_type=ram_type)
    mixer.blend('inventory.ComputerRamRelation', computer=computer, ram=ram)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/' + str(computer.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, "RAM Modules:"))


def test_computer_detail_view_raid_relation(create_admin_user):
    create_admin_user()
    computer = mixer.blend('inventory.Computer', customer=mixer.SELECT)
    raid = mixer.blend('inventory.RaidType')
    disk = mixer.blend('inventory.Disk')
    disks = mixer.blend('inventory.DisksInRaid', raid=raid, disk=disk)
    mixer.blend('inventory.RaidInComputer', computer=computer, raid=disks)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/' + str(computer.id) + '/')
    assert response.status_code == 200 and helper.in_content(response, "RAID")


def test_computer_detail_view_cpu_relation(create_admin_user):
    create_admin_user()
    computer = mixer.blend('inventory.Computer', customer=mixer.SELECT)
    cpu = mixer.blend('inventory.Cpu', cpu_typ=mixer.SELECT)
    mixer.blend('inventory.ComputerCpuRelation', cpu=cpu, computer=computer)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/' + str(computer.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, cpu.name))


def test_computer_detail_view_no_permission(create_admin_user):
    customer = mixer.blend('inventory.Customer')
    computer = mixer.blend('inventory.Computer', customer=customer)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/' + str(computer.id) + '/')
    assert response.status_code == 200

