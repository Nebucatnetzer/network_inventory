import pytest

from django.test import Client
from mixer.backend.django import mixer

import helper
from inventory.models import Customer

pytestmark = pytest.mark.django_db


def test_customer_user_table_not_logged_in():
    response = Client().get('/customer/1/users/')
    assert response.status_code == 302 and 'login' in response.url


def test_customer_user_table(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    client = Client()
    client.login(username="novartis-admin", password="password")
    user = mixer.blend('inventory.User', customer=mixer.SELECT)
    ad_group = mixer.blend('inventory.AdGroup')
    mail_group = mixer.blend('inventory.MailGroup')
    mixer.blend('inventory.UserInAdGroup', user=user, group=ad_group)
    mixer.blend('inventory.UserInMailGroup', user=user, group=mail_group)
    response = client.get('/customer/' + str(customer.id) + '/users/')
    assert (response.status_code == 200
            and helper.in_content(response, user.name)
            and helper.in_content(response, ad_group)
            and helper.in_content(response, mail_group)
            and helper.in_content(response, user.primary_mail))


def test_customer_user_table_no_user(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/customer/' + str(customer.id) + '/users/')
    assert (response.status_code == 200
            and helper.not_in_content(response, customer))


def test_customer_user_table_no_permission(create_admin_user):
    create_admin_user()
    customer = Customer.objects.create(name='Nestle')
    client = Client()
    client.login(username="novartis-admin", password="password")
    mixer.blend('inventory.User', customer=customer)
    response = client.get('/customer/' + str(customer.id) + '/users/')
    assert response.status_code == 403


def test_customer_user_table_multiple_users(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    client = Client()
    client.login(username="novartis-admin", password="password")
    user1 = mixer.blend('inventory.User', customer=mixer.SELECT)
    user2 = mixer.blend('inventory.User', customer=mixer.SELECT)
    response = client.get('/customer/' + str(customer.id) + '/users/')
    assert (response.status_code == 200
            and helper.in_content(response, user1)
            and helper.in_content(response, user2))
