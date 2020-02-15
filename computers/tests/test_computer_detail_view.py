import pytest
from mixer.backend.django import mixer

from django.test import Client

from core.tests import helper

pytestmark = pytest.mark.django_db


def test_computer_detail_view_not_logged_in():
    response = Client().get('/computer/1/')
    assert response.status_code == 302 and 'login' in response.url


def test_computer_detail_view(create_admin_user):
    create_admin_user()
    computer = mixer.blend('computers.Computer', customer=mixer.SELECT,
                           os=mixer.SELECT)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/' + str(computer.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, computer))


def test_computer_detail_view_not_found(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/230/')
    assert response.status_code == 404


def test_computer_detail_view_ram_relation(create_admin_user):
    create_admin_user()
    computer = mixer.blend('computers.Computer', customer=mixer.SELECT)
    ram_type = mixer.blend('computers.RamType')
    ram = mixer.blend('computers.Ram', ram_type=ram_type)
    mixer.blend('computers.ComputerRamRelation', computer=computer, ram=ram)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/' + str(computer.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, "RAM Modules:"))


def test_computer_detail_view_raid_relation(create_admin_user):
    create_admin_user()
    computer = mixer.blend('computers.Computer', customer=mixer.SELECT)
    raid_type = mixer.blend('computers.RaidType')
    disk = mixer.blend('computers.Disk')
    raid = mixer.blend('computers.Raid',
                       computer=computer,
                       raid_type=raid_type)
    mixer.blend('computers.DisksInRaid', raid=raid, disk=disk)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/' + str(computer.id) + '/')
    assert response.status_code == 200 and helper.in_content(response, "RAID")


def test_computer_detail_view_cpu_relation(create_admin_user):
    create_admin_user()
    computer = mixer.blend('computers.Computer', customer=mixer.SELECT)
    cpu = mixer.blend('computers.Cpu', cpu_typ=mixer.SELECT)
    mixer.blend('computers.ComputerCpuRelation', cpu=cpu, computer=computer)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/' + str(computer.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, cpu))


def test_computer_detail_view_no_permission(create_admin_user):
    create_admin_user()
    customer = mixer.blend('customers.Customer')
    computer = mixer.blend('computers.Computer', customer=customer)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/computer/' + str(computer.id) + '/')
    assert response.status_code == 403