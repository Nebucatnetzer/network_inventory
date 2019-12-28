import pytest
from mixer.backend.django import mixer

from django.test import Client

import helper
from inventory.models import Customer

pytestmark = pytest.mark.django_db


def test_customer_computer_table_not_logged_in():
    response = Client().get('/customer/1/computers/')
    assert response.status_code == 302 and 'login' in response.url


def test_customer_computer_table(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    client = Client()
    client.login(username="novartis-admin", password="password")
    computer = mixer.blend('inventory.Computer', customer=mixer.SELECT)
    response = client.get('/customer/' + str(customer.id) + '/computers/')
    assert (response.status_code == 200
            and helper.in_content(response, computer))


def test_customer_computer_table_no_computer(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/customer/' + str(customer.id) + '/computers/')
    assert (response.status_code == 200
            and helper.not_in_content(response, "Novartis PC"))


def test_customer_computer_table_no_permission(create_admin_user):
    create_admin_user()
    customer = Customer.objects.create(name='Nestle')
    client = Client()
    client.login(username="novartis-admin", password="password")
    mixer.blend('inventory.Computer', customer=customer)
    response = client.get('/customer/' + str(customer.id) + '/computers/')
    assert response.status_code == 403

