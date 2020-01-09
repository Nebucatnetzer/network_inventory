import pytest
from mixer.backend.django import mixer

from django.test import Client

from core.tests import helper

from customers.models import Customer

pytestmark = pytest.mark.django_db


def test_customer_backup_table_not_logged_in():
    response = Client().get('/customer/1/backups/')
    assert response.status_code == 302 and 'login' in response.url


def test_customer_backup_table(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    client = Client()
    client.login(username="novartis-admin", password="password")
    computer = mixer.blend('inventory.Computer', customer=customer)
    backup = mixer.blend('inventory.Backup', computer=computer)
    response = client.get('/customer/' + str(customer.id) + '/backups/')
    assert (response.status_code == 200
            and helper.in_content(response, backup.name))


def test_customer_backup_table_no_backup(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/customer/' + str(customer.id) + '/backups/')
    assert response.status_code == 200


def test_customer_backup_table_no_permission(create_admin_user):
    create_admin_user()
    customer = Customer.objects.create(name='Nestle')
    client = Client()
    client.login(username="novartis-admin", password="password")
    computer = mixer.blend('inventory.Computer', customer=customer)
    mixer.blend('inventory.Backup', computer=computer)
    response = client.get('/customer/' + str(customer.id) + '/backups/')
    assert response.status_code == 403


def test_customer_backup_table_with_multiple_backups(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    client = Client()
    client.login(username="novartis-admin", password="password")
    computer = mixer.blend('inventory.Computer', customer=customer)
    backup1 = mixer.blend('inventory.Backup', computer=computer)
    backup2 = mixer.blend('inventory.Backup', computer=computer)
    response = client.get('/customer/' + str(customer.id) + '/backups/')
    assert (response.status_code == 200
            and helper.in_content(response, backup1)
            and helper.in_content(response, backup2))
