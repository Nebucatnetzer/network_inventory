from mixer.backend.django import mixer

import pytest

from core import utils

from customers.models import Customer
from devices.models import Device

pytestmark = pytest.mark.django_db


def test_objects_for_allowed_customers(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    admin = fixture['admin']
    objects = utils.objects_for_allowed_customers(
        Customer, user=admin)
    assert objects[0] == customer


def test_objects_for_allowed_customers_device(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    admin = fixture['admin']
    device = mixer.blend(Device, customer=customer)
    objects = utils.objects_for_allowed_customers(
        Device, user=admin)
    assert objects[0] == device


def test_get_all_objects_for_unallowed_customers(create_admin_user):
    fixture = create_admin_user()
    customer = mixer.blend(Customer)
    admin = fixture['admin']
    objects = utils.objects_for_allowed_customers(
        Customer, user=admin)
    assert customer not in objects


def test_get_all_objects_for_unallowed_customers_device(create_admin_user):
    fixture = create_admin_user()
    customer = mixer.blend(Customer)
    admin = fixture['admin']
    device = mixer.blend(Device, customer=customer)
    objects = utils.objects_for_allowed_customers(
        Device, user=admin)
    assert device not in objects
