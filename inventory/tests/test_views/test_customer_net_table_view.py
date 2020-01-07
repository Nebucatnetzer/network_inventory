import pytest
from mixer.backend.django import mixer

from django.test import Client

import helper

from customer.models import Customer

pytestmark = pytest.mark.django_db


def test_customer_net_table_not_logged_in():
    response = Client().get('/customer/1/nets/')
    assert response.status_code == 302 and 'login' in response.url


def test_customer_net_table(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="novartis-admin", password="password")
    net = mixer.blend('inventory.Net', customer=mixer.SELECT)
    response = client.get('/customer/' + str(net.customer.id) + '/nets/')
    assert (response.status_code == 200
            and helper.in_content(response, net))


def test_customer_net_table_no_net(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/customer/' + str(customer.id) + '/nets/')
    assert response.status_code == 200


def test_customer_net_table_no_permission(create_admin_user):
    create_admin_user()
    customer = Customer.objects.create(name='Nestle')
    client = Client()
    client.login(username="novartis-admin", password="password")
    mixer.blend('inventory.Net', customer=customer)
    response = client.get('/customer/' + str(customer.id) + '/nets/')
    assert response.status_code == 403
