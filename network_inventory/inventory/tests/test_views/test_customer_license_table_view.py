import pytest

from django.test import Client
from mixer.backend.django import mixer

import helper
from inventory.models import Customer


pytestmark = pytest.mark.django_db


def test_customer_license_table_not_logged_in():
    response = Client().get('/customer/1/licenses/')
    assert response.status_code == 302 and 'login' in response.url


def test_customer_license_table(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    client = Client()
    client.login(username="novartis-admin", password="password")
    license = mixer.blend('inventory.UserLicense', customer=customer,
                          software=mixer.SELECT, key=mixer.RANDOM,
                          max_allowed_users=mixer.RANDOM)
    response = client.get('/customer/' + str(customer.id) + '/licenses/')
    assert (response.status_code == 200
            and helper.in_content(response, license.software)
            and helper.in_content(response, license.key)
            and helper.in_content(response, license.max_allowed_users))


def test_customer_license_table_no_license(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    client = Client()
    client.login(username="novartis-admin", password="password")
    response = client.get('/customer/' + str(customer.id) + '/licenses/')
    assert (response.status_code == 200
            and helper.not_in_content(response, customer))


def test_customer_license_table_no_permission(create_admin_user):
    create_admin_user()
    customer = Customer.objects.create(name='Nestle')
    client = Client()
    client.login(username="novartis-admin", password="password")
    mixer.blend('inventory.UserLicense', customer=customer)
    response = client.get('/customer/' + str(customer.id) + '/licenses/')
    assert response.status_code == 403


def test_customer_license_table_multiple_licenses(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    user = mixer.blend('inventory.User')
    client = Client()
    client.login(username="novartis-admin", password="password")
    license1 = mixer.blend('inventory.UserLicense', customer=customer,
                           software=mixer.SELECT, key=mixer.RANDOM,
                           max_allowed_users=mixer.RANDOM)
    license2 = mixer.blend('inventory.UserLicense', customer=customer,
                           software=mixer.SELECT, key=mixer.RANDOM,
                           max_allowed_users=mixer.RANDOM)
    mixer.blend('inventory.LicenseWithUser', user=user, license=mixer.SELECT)
    response = client.get('/customer/' + str(customer.id) + '/licenses/')
    assert (response.status_code == 200
            and helper.in_content(response, license1.software)
            and helper.in_content(response, license1.key)
            and helper.in_content(response, license1.max_allowed_users)
            and helper.in_content(response, license2.software)
            and helper.in_content(response, license2.key)
            and helper.in_content(response, license2.max_allowed_users))
