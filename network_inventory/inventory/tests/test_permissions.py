from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import Client
from guardian.shortcuts import assign_perm
import pytest

from inventory.models import Customer, Computer


def create_users():
    User = get_user_model()
    novartis = User.objects.create_user('novartis_admin',
                                          'novartis_admin@novartis.com',
                                          'password',
                                          is_staff=True)
    nestle = User.objects.create_user('nestle_admin',
                                          'nestle_admin@nestle.com',
                                          'password',
                                          is_staff=True)
    return novartis, nestle


def create_groups():
    novartis_admin_group = Group.objects.create(name='NovartisAdmins')
    nestle_admin_group = Group.objects.create(name='NestleAdmins')
    return novartis_admin_group, nestle_admin_group


def create_customers():
    novartis = Customer.objects.create(name='Novartis')
    nestle = Customer.objects.create(name='Nestle')
    return novartis, nestle


def create_computers():
    Computer.objects.create(name='novartis-pc1',
                            customer=Customer.objects.get(name='Novartis'))
    Computer.objects.create(name='nestle-pc1',
                            customer=Customer.objects.get(name='Nestle'))


@pytest.mark.django_db
def test_something():
    novartis_admin_group, nestle_admin_group = create_groups()
    novartis_admin, nestle_admin = create_users()
    novartis, nestle = create_customers()
    create_computers()
    novartis_admin.groups.add(novartis_admin_group)
    nestle_admin.groups.add(nestle_admin_group)
    assign_perm('view_customer', novartis_admin, novartis)
    assign_perm('view_customer', nestle_admin, nestle)

    novartis_client = Client()
    nestle_client = Client()
    response = novartis_client.post('/admin/',
                                    {'username': 'novartis_admin',
                                     'password': 'password'})
    response = novartis_client.get('/')
    print(response.content)
    assert False
