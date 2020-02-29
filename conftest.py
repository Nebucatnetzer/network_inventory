import pytest
from mixer.backend.django import mixer

from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from guardian.shortcuts import assign_perm


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'backups.yaml')
        call_command('loaddata', 'computers.yaml')
        call_command('loaddata', 'core.yaml')
        call_command('loaddata', 'devices.yaml')
        call_command('loaddata', 'nets.yaml')
        call_command('loaddata', 'softwares.yaml')


@pytest.fixture
def create_admin_user():
    def _create_admin_user():
        User = get_user_model()
        admin = User.objects.create_user("novartis-admin", "admin@novartis.com",
                                         "password", is_staff=True)
        customer = mixer.blend('customers.Customer')
        group = Group.objects.create(name="Novartis Admin")
        admin.groups.add(group)
        assign_perm('view_customer', admin, customer)
        result = {}
        result['admin'] = admin
        result['customer'] = customer
        result['group'] = group
        return result
    return _create_admin_user
