from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import Client
from guardian.shortcuts import assign_perm
import pytest

from inventory.models import Customer, Computer


def create_users():
    User = get_user_model()
    customer_c = User.objects.create_user('customer_c',
                                          'c@ccompany.com',
                                          'password',
                                          is_staff=True)
    customer_h = User.objects.create_user('customer_h',
                                          'h@hcompany.com',
                                          'password',
                                          is_staff=True)
    return customer_c, customer_h


def create_groups():
    cadmin = Group.objects.create(name='CAdmin')
    hadmin = Group.objects.create(name='HAdmin')
    return cadmin, hadmin


def create_customers():
    c = Customer.objects.create(name='C')
    h = Customer.objects.create(name='H')
    return c, h


def create_computers():
    Computer.objects.create(name='c-pc1',
                            customer=Customer.objects.get(name='C'))
    Computer.objects.create(name='h-pc1',
                            customer=Customer.objects.get(name='H'))


@pytest.mark.django_db
def test_something():
    cadmin, hadmin = create_groups()
    customer_c, customer_h = create_users()
    c, h = create_customers()
    create_computers()
    customer_c.groups.add(cadmin)
    customer_h.groups.add(hadmin)
    assign_perm('view_customer', cadmin, c)
    assign_perm('view_customer', hadmin, h)

    c_client = Client()
    h_client = Client()
    response = c_client.post('/admin/',
                             {'username': 'customer_c',
                              'password': 'password'})
    response = c_client.get('/')
    print(response.content)
    assert False
