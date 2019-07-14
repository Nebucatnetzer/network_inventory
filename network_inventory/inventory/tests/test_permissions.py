from django.test import Client
from guardian.shortcuts import assign_perm
import pytest


@pytest.mark.django_db
def test_customer_permissions(make_admin_users, make_customers,
                              make_admin_groups, make_computers):
    nestle = 'Nestle'
    novartis = 'Novartis'
    customer_names = [novartis, nestle]
    admins = make_admin_users(customer_names)
    customers = make_customers(customer_names)
    groups = make_admin_groups(customer_names)
    computers = make_computers(customer_names)

    admins[novartis].groups.add(groups[novartis])
    admins[nestle].groups.add(groups[nestle])
    assign_perm('view_customer', admins[novartis], customers[novartis])
    assign_perm('view_customer', admins[nestle], customers[nestle])

    novartis_client = Client()
    nestle_client = Client()
    response = novartis_client.post('/admin/', follow=True)
    loginresponse = novartis_client.login(username=admins[novartis].username,
                                          password='password')
    response = novartis_client.get('/')
    print(response.content.decode('utf8'))
    assert (novartis in response.content.decode('utf8') and
            nestle not in response.content.decode('utf8'))
