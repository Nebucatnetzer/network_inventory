import pytest

from django.test import Client
from mixer.backend.django import mixer

from core.tests import helper
from customers.models import Customer

pytestmark = pytest.mark.django_db


def test_customer_mail_group_table_not_logged_in():
    response = Client().get('/customer/1/groups/')
    assert response.status_code == 302 and 'login' in response.url


def test_customer_mail_group_table(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    client = Client()
    client.login(username="pharma-admin", password="password")
    mail_group = mixer.blend('users.MailGroup', customer=customer)
    response = client.get('/customer/' + str(customer.id) + '/groups/')
    assert (response.status_code == 200
            and helper.in_content(response, mail_group))


def test_customer_mail_group_table_no_group(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get('/customer/' + str(customer.id) + '/groups/')
    assert response.status_code == 200


def test_customer_mail_group_table_no_permission(create_admin_user):
    create_admin_user()
    customer = Customer.objects.create(name='Water Corp.')
    client = Client()
    client.login(username="pharma-admin", password="password")
    mixer.blend('users.MailGroup', customer=customer)
    response = client.get('/customer/' + str(customer.id) + '/groups/')
    assert response.status_code == 403


def test_customer_mail_group_table_multiple_groups(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    client = Client()
    client.login(username="pharma-admin", password="password")
    group1 = mixer.blend('users.MailGroup', customer=mixer.SELECT)
    group2 = mixer.blend('users.MailGroup', customer=mixer.SELECT)
    response = client.get('/customer/' + str(customer.id) + '/groups/')
    assert (response.status_code == 200
            and helper.in_content(response, group1.name)
            and helper.in_content(response, group2.name))
