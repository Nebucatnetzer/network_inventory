from django.test import Client

from mixer.backend.django import mixer

import pytest

from core.tests import helper

pytestmark = pytest.mark.django_db


def test_customer_create_view(create_admin_user):
    create_admin_user()
    data = {'name': 'Big Pharma',
            'description': 'Some text.'}
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.post('/create/customer/', data)
    assert response.status_code == 200


def test_load_customer_create_view(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get('/create/customer/')
    assert response.status_code == 200


def test_create_duplicate_customer(create_admin_user):
    create_admin_user()
    customer = mixer.blend('customers.Customer')
    data = {'name': customer.name,
            'description': customer.description}
    client = Client()
    client.login(username="pharma-admin", password="password")
    client.post('/create/customer/', data)
    response = client.post('/create/customer/', data)
    assert (response.status_code == 200
            and helper.in_content(response, "Customer with this Name already exists."))
