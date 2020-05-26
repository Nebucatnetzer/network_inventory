from django.test import Client
from mixer.backend.django import mixer
import pytest


pytestmark = pytest.mark.django_db


def test_computer_create_view(create_admin_user):
    fixture = create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    data = {'name': 'Test Computer',
            'customer': fixture['customer'].id}
    url = '/customer/{}/create/computer/'.format(fixture['customer'].id)
    response = client.post(url, data)
    assert response.status_code == 302


def test_computer_delete_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend('computers.Computer')
    response = client.post('/delete/computer/{}/'.format(computer.pk))
    assert response.status_code == 302


def test_computer_update_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend('computers.Computer', customer=mixer.SELECT)
    data = {'name': 'Foo',
            'description': '',
            'serialnumber': '',
            'category': '',
            'owner': '',
            'customer': computer.customer.id,
            'manufacturer': '',
            'model': '',
            'location': '',
            'user': '',
            'installation_date': ''}
    response = client.post('/update/computer/{}/'.format(computer.pk), data)
    assert response.status_code == 302
    computer.refresh_from_db()
    assert computer.name == data['name']
