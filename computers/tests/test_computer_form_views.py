from django.test import Client
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
