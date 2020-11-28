import pytest

from django.test import Client
from mixer.backend.django import mixer

from core.tests import helper
from customers.models import Customer


pytestmark = pytest.mark.django_db


def test_customer_license_table_not_logged_in():
    response = Client().get('/customer/1/licenses/')
    assert response.status_code == 302 and 'login' in response.url


def test_customer_license_table(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    client = Client()
    user = mixer.blend('users.User')
    computer = mixer.blend('computers.Computer')
    client.login(username="pharma-admin", password="password")
    user_license = mixer.blend('licenses.UserLicense', customer=customer,
                               software=mixer.SELECT, key=mixer.RANDOM,
                               max_allowed_users=mixer.RANDOM)
    computer_license = mixer.blend('licenses.ComputerLicense',
                                   customer=customer,
                                   software=mixer.SELECT, key=mixer.RANDOM,
                                   max_allowed_computers=mixer.RANDOM)
    mixer.blend('licenses.LicenseWithUser', user=user, license=user_license)
    mixer.blend('licenses.LicenseWithComputer',
                computer=computer,
                license=computer_license)
    url = '/customer/{}/licenses/'.format(customer.id)
    response = client.get(url)
    assert (response.status_code == 200
            and helper.in_content(response, user_license.software)
            and helper.in_content(response, user_license.key)
            and helper.in_content(response, user_license.max_allowed_users)
            and helper.in_content(response, computer_license.software)
            and helper.in_content(response, computer_license.key)
            and helper.in_content(
                response, computer_license.max_allowed_computers))


def test_customer_license_table_no_license(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get('/customer/' + str(customer.id) + '/licenses/')
    assert (response.status_code == 200
            and helper.not_in_content(response, customer))


def test_customer_license_table_no_permission(create_admin_user):
    create_admin_user()
    customer = Customer.objects.create(name='Water Corp.')
    client = Client()
    client.login(username="pharma-admin", password="password")
    mixer.blend('licenses.UserLicense', customer=customer)
    response = client.get('/customer/' + str(customer.id) + '/licenses/')
    assert response.status_code == 403


def test_customer_license_table_multiple_licenses(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    user1 = mixer.blend('users.User')
    user2 = mixer.blend('users.User')
    client = Client()
    client.login(username="pharma-admin", password="password")
    license1 = mixer.blend('licenses.UserLicense', customer=customer,
                           software=mixer.SELECT, key=mixer.RANDOM,
                           max_allowed_users=mixer.RANDOM)
    license2 = mixer.blend('licenses.UserLicense', customer=customer,
                           software=mixer.SELECT, key=mixer.RANDOM,
                           max_allowed_users=mixer.RANDOM)
    mixer.blend('licenses.LicenseWithUser', user=user1, license=license1)
    mixer.blend('licenses.LicenseWithUser', user=user2, license=license2)
    response = client.get('/customer/' + str(customer.id) + '/licenses/')
    assert (response.status_code == 200
            and helper.in_content(response, license1.software)
            and helper.in_content(response, license1.key)
            and helper.in_content(response, license1.max_allowed_users)
            and helper.in_content(response, license2.software)
            and helper.in_content(response, license2.key)
            and helper.in_content(response, license2.max_allowed_users))
