from django.test import Client
from mixer.backend.django import mixer
import pytest

from core.tests import helper


pytestmark = pytest.mark.django_db


def test_load_htmx_create_location_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    url = '/create/location/'
    response = client.get(url)
    assert (response.status_code == 200
            and helper.in_content(response, 'Add Location'))


def test_htmx_create_location_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    data = {"name": mixer.faker.name(),
            "save_location": 1}
    response = client.post('/create/location/', data)
    assert (response.status_code == 200
            and helper.in_content(response, data["name"]))


def test_htmx_create_location_view_invalid_form(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    data = {"name": "",
            "save_location": 1}
    response = client.post('/create/location/', data)
    assert (response.status_code == 200
            and helper.in_content(response, "This field is required."))
