import pytest
from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from inventory.models import Customer, Computer


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'inventory.yaml')


@pytest.fixture
def make_admin_users():
    def _make_admin_users(customer_names):
        admins = {}
        for name in customer_names:
            User = get_user_model()
            username = name.lower() + '_admin'
            domain = name.lower() + '.com'
            admins[name] = User.objects.create_user(
                                username,
                                username + '@' + domain,
                                'password',
                                is_staff=True)
        return admins
    return _make_admin_users


@pytest.fixture
def make_customers():
    def _make_customers(customer_names):
        customers = {}
        for name in customer_names:
            customers[name] = Customer.objects.create(name=name)
        return customers
    return _make_customers


@pytest.fixture
def make_admin_groups():
    def _make_admin_groups(customer_names):
        groups = {}
        for name in customer_names:
            groups[name] = Group.objects.create(name=name)
        return groups
    return _make_admin_groups


@pytest.fixture
def make_computers():
    def _make_computers(customer_names):
        computers = {}
        for name in customer_names:
            computers[name] = Computer.objects.create(
                                name=name.lower() + '-pc1',
                                customer=Customer.objects.get(name=name))
        return computers
    return _make_computers
