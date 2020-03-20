import pytest
from mixer.backend.django import mixer

from django.test import Client

from core.tests import helper

pytestmark = pytest.mark.django_db


def test_computer_list_view_not_logged_in():
    response = Client().get('/computers/all/')
    assert response.status_code == 302 and 'login' in response.url


def test_computer_list_view_no_computers(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get('/computers/all/')
    assert response.status_code == 200


def test_computer_list_view(create_admin_user):
    create_admin_user()
    computer = mixer.blend('computers.Computer', customer=mixer.SELECT)
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get('/computers/all/')
    assert (response.status_code == 200
            and helper.in_content(response, computer))
