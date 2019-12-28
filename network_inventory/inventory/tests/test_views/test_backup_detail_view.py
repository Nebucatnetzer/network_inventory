import pytest
from mixer.backend.django import mixer
from django.test import Client

import helper

pytestmark = pytest.mark.django_db


def test_backup_detail_view_not_logged_in():
    response = Client().get('/backup/1/')
    assert response.status_code == 302 and 'login' in response.url


def test_backup_detail_view(create_admin_user):
    create_admin_user()
    mixer.blend('inventory.Computer')
    backup = mixer.blend('inventory.Backup', computer=mixer.SELECT)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/backup/' + str(backup.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, backup))


def test_backup_detail_view_not_found(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/backup/100/')
    assert response.status_code == 200
