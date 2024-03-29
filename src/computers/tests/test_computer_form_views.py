from django.test import Client
from mixer.backend.django import mixer
import pytest


pytestmark = pytest.mark.django_db


def test_computer_create_view(create_admin_user):
    fixture = create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    data = {"name": "Test Computer", "customer": fixture["customer"].id}
    url = "/customer/{}/create/computer/".format(fixture["customer"].id)
    response = client.post(url, data)
    assert response.status_code == 302


def test_computer_delete_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend("computers.Computer")
    response = client.post("/delete/computer/{}/".format(computer.pk))
    assert response.status_code == 302


def test_computer_update_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend("computers.Computer", customer=mixer.SELECT)
    data = {
        "name": "Foo",
        "description": "",
        "serialnumber": "",
        "category": "",
        "owner": "",
        "customer": computer.customer.id,
        "manufacturer": "",
        "model": "",
        "location": "",
        "user": "",
        "installation_date": "",
    }
    response = client.post("/update/computer/{}/".format(computer.pk), data)
    assert response.status_code == 302
    computer.refresh_from_db()
    assert computer.name == data["name"]


def test_ram_relation_create_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend("computers.Computer", customer=mixer.SELECT)
    ram = mixer.blend("computers.Ram")
    data = {"computer": computer.id, "ram": ram.id, "amount": 1}
    url = "/computer/{}/create/ram-relation/".format(computer.id)
    response = client.post(url, data)
    assert response.status_code == 302


def test_cpu_relation_create_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend("computers.Computer", customer=mixer.SELECT)
    cpu = mixer.blend("computers.Cpu")
    data = {"computer": computer.id, "cpu": cpu.id, "amount": 1}
    url = "/computer/{}/create/cpu-relation/".format(computer.id)
    response = client.post(url, data)
    assert response.status_code == 302


def test_gpu_relation_create_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend("computers.Computer", customer=mixer.SELECT)
    gpu = mixer.blend("computers.gpu")
    data = {"computer": computer.id, "gpu": gpu.id, "amount": 1}
    url = "/computer/{}/create/gpu-relation/".format(computer.id)
    response = client.post(url, data)
    assert response.status_code == 302


def test_disk_relation_create_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend("computers.Computer", customer=mixer.SELECT)
    disk = mixer.blend("computers.Disk")
    data = {"computer": computer.id, "disk": disk.id, "amount": 1}
    url = "/computer/{}/create/disk-relation/".format(computer.id)
    response = client.post(url, data)
    assert response.status_code == 302


def test_software_relation_create_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend("computers.Computer", customer=mixer.SELECT)
    software = mixer.blend("softwares.Software")
    data = {"computer": computer.id, "software": software.id, "amount": 1}
    url = "/computer/{}/create/software-relation/".format(computer.id)
    response = client.post(url, data)
    assert response.status_code == 302


def test_raid_create_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend("computers.Computer", customer=mixer.SELECT)
    data = {
        "computer": computer.id,
    }
    url = "/computer/{}/create/raid/".format(computer.id)
    response = client.post(url, data)
    assert response.status_code == 302


def test_ram_relation_delete_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend("computers.Computer", customer=mixer.SELECT)
    ram = mixer.blend("computers.Ram")
    ram_relation = mixer.blend(
        "computers.ComputerRamRelation", computer=computer, ram=ram, amount=1
    )
    url = "/delete/ram-relation/{}/".format(ram_relation.id)
    response = client.post(url)
    assert response.status_code == 302


def test_cpu_relation_delete_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend("computers.Computer", customer=mixer.SELECT)
    cpu = mixer.blend("computers.Cpu")
    cpu_relation = mixer.blend(
        "computers.ComputerCpuRelation", computer=computer, cpu=cpu, amount=1
    )
    url = "/delete/cpu-relation/{}/".format(cpu_relation.id)
    response = client.post(url)
    assert response.status_code == 302


def test_gpu_relation_delete_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend("computers.Computer", customer=mixer.SELECT)
    gpu = mixer.blend("computers.Gpu")
    gpu_relation = mixer.blend(
        "computers.ComputerGpuRelation", computer=computer, gpu=gpu, amount=1
    )
    url = "/delete/gpu-relation/{}/".format(gpu_relation.id)
    response = client.post(url)
    assert response.status_code == 302


def test_disk_relation_delete_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend("computers.Computer", customer=mixer.SELECT)
    disk = mixer.blend("computers.disk")
    disk_relation = mixer.blend(
        "computers.ComputerDiskRelation",
        computer=computer,
        disk=disk,
        amount=1,
    )
    url = "/delete/disk-relation/{}/".format(disk_relation.id)
    response = client.post(url)
    assert response.status_code == 302


def test_software_relation_delete_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend("computers.Computer", customer=mixer.SELECT)
    software = mixer.blend("softwares.Software")
    software_relation = mixer.blend(
        "computers.ComputerSoftwareRelation",
        computer=computer,
        software=software,
    )
    url = "/delete/software-relation/{}/".format(software_relation.id)
    response = client.post(url)
    assert response.status_code == 302


def test_raid_delete_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend("computers.Computer", customer=mixer.SELECT)
    raid = mixer.blend("computers.Raid", computer=computer)
    url = "/delete/raid/{}/".format(raid.id)
    response = client.post(url)
    assert response.status_code == 302
