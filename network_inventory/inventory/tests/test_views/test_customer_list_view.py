import pytest

from django.test import Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from guardian.shortcuts import assign_perm

from mixer.backend.django import mixer

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
            and helper.in_content(response, customer))


def test_customer_list_view_multiple_customers(create_admin_user):
    fixture = create_admin_user()
    customer1 = fixture['customer']
    customer2 = mixer.blend('inventory.Customer')
    assign_perm('view_customer', fixture['admin'], customer2)
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/')
    assert (response.status_code == 200
            and helper.in_content(response, customer1)
            and helper.in_content(response, customer1.id)
            and helper.in_content(response, customer1)
            and helper.in_content(response, customer2.id))
