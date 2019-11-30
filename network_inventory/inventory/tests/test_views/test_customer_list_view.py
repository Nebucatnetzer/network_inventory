import pytest

from django.test import Client
from django.contrib.auth import get_user_model

import helper

pytestmark = pytest.mark.django_db


def test_customer_list_view_not_logged_in():
    response = Client().get('/')
    assert response.status_code == 302 and 'login' in response.url


def test_customer_list_view_no_customer():
    User = get_user_model()
    User.objects.create_user("novartis-admin", "admin@novartis.com",
                             "password", is_staff=True)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/')
    assert response.status_code == 200


def test_customer_list_view(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/')
    assert (response.status_code == 200
            and helper.in_content(response, customer.name))
