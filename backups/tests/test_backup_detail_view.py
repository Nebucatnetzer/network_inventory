import pytest
from mixer.backend.django import mixer
from django.test import Client

from core.tests import helper
from customers.models import Customer

pytestmark = pytest.mark.django_db


def test_backup_detail_view_not_logged_in():
    response = Client().get('/backup/1/')
    assert response.status_code == 302 and 'login' in response.url


def test_backup_detail_view(create_admin_user):
    create_admin_user()
    mixer.blend('inventory.Computer', customer=mixer.SELECT)
    backup = mixer.blend('backups.Backup', computer=mixer.SELECT)
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
    assert response.status_code == 404


def test_customer_computer_table_no_permission(create_admin_user):
    create_admin_user()
    customer = Customer.objects.create(name='Nestle')
    client = Client()
    client.login(username="novartis-admin", password="password")
    mixer.blend('inventory.Computer', customer=customer)
    backup = mixer.blend('backups.Backup', computer=mixer.SELECT)
    response = client.get('/backup/' + str(backup.id) + '/')
    assert response.status_code == 403


def test_backup_detail_view_with_target_device(create_admin_user):
    create_admin_user()
    source_computer = mixer.blend('inventory.Computer', customer=mixer.SELECT)
    target_computer = mixer.blend('inventory.Computer', customer=mixer.SELECT)
    backup = mixer.blend('backups.Backup', computer=source_computer,
                         software=mixer.SELECT, method=mixer.SELECT)
    mixer.blend('backups.TargetDevice', device=target_computer,
                backup=mixer.SELECT)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/backup/' + str(backup.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, backup)
            and helper.in_content(response, target_computer))


def test_backup_detail_view_with_notification(create_admin_user):
    create_admin_user()
    mixer.blend('inventory.Computer', customer=mixer.SELECT)
    backup = mixer.blend('backups.Backup', computer=mixer.SELECT)
    notification = mixer.blend('backups.Notification')
    mixer.blend('backups.NotificationFromBackup',
                backup=backup,
                notification=notification)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/backup/' + str(backup.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, notification))
