import pytest
from mixer.backend.django import mixer

from django.test import Client
from django.contrib.auth import get_user_model

import helper

pytestmark = pytest.mark.django_db


def test_customer_detail_view_not_logged_in():
    response = Client().get('/customer/1/')
    assert response.status_code == 302 and 'login' in response.url


def test_customer_detail_view_not_found(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/customer/230/')
    assert response.status_code == 404


def test_customer_detail_view(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/customer/' + str(customer.id) + '/')
    assert (response.status_code == 200
            and helper.in_content(response, customer.name))


def test_customer_detail_view_no_permissions():
    User = get_user_model()
    admin = User.objects.create_user("novartis-admin", "admin@novartis.com",
                                     "password", is_staff=True)
    client = Client()
    customer = mixer.blend('inventory.Customer')
    client.login(username="novartis-admin", password="password")
    response = client.get('/customer/' + str(customer.id) + '/')
    assert response.status_code == 302 and 'login' in response.url
