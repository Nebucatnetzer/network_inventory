from django.test import Client
from mixer.backend.django import mixer
import pytest


pytestmark = pytest.mark.django_db


def test_license_relation_create_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend('computers.Computer', customer=mixer.SELECT)
    license = mixer.blend('licenses.ComputerLicense')
    data = {
        'computer': computer.id,
        'license': license.id,
        'amount': 1
    }
    url = '/create/license-with/computer/{}/'.format(computer.id)
    response = client.post(url, data)
    assert response.status_code == 302


