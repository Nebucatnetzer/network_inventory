from django.test import Client
from mixer.backend.django import mixer
import pytest


pytestmark = pytest.mark.django_db


def test_backup_with_computer_create_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend("computers.Computer", customer=mixer.SELECT)
    target_device = mixer.blend("computers.Computer", customer=mixer.SELECT)
    data = {
        "name": "foo",
        "computer": computer.id,
        "amount": 1,
        "exec_time": "12:00",
        "method": 1,
        "exec_days": 3,
        "target_device": target_device.id,
    }
    url = "/create/backup-for-computer/{}/".format(computer.id)
    response = client.post(url, data)
    assert response.status_code == 302


def test_backup_with_computer_delete_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend("computers.Computer", customer=mixer.SELECT)
    backup = mixer.blend("backups.Backup", computer=computer)
    url = "/delete/backup/{}/".format(backup.id)
    response = client.post(url)
    assert response.status_code == 302
