from django.http import Http404
from mixer.backend.django import mixer

import pytest

from core import utils

from customers.models import Customer
from devices.models import Device

pytestmark = pytest.mark.django_db


def test_get_objects_for_customer_with_customer(create_admin_user):
    fixture = create_admin_user()
    customer = fixture["customer"]
    admin = fixture["admin"]
    with pytest.raises(Exception):
        utils.get_objects_for_customer(Customer, user=admin, customer_pk=customer.id)


def test_get_objects_for_customer_device(create_admin_user):
    fixture = create_admin_user()
    customer = fixture["customer"]
    admin = fixture["admin"]
    device = mixer.blend(Device, customer=customer)
    objects = utils.get_objects_for_customer(
        Device, user=admin, customer_pk=customer.id
    )
    assert objects[0] == device


def test_get_all_objects_for_unallowed_customers(create_admin_user):
    fixture = create_admin_user()
    customer = mixer.blend(Customer)
    admin = fixture["admin"]
    with pytest.raises(Http404):
        utils.get_objects_for_customer(Customer, user=admin, customer_pk=customer.id)


def test_get_all_objects_for_unallowed_customers_device(create_admin_user):
    fixture = create_admin_user()
    customer = mixer.blend(Customer)
    admin = fixture["admin"]
    mixer.blend(Device, customer=customer)
    with pytest.raises(Http404):
        utils.get_objects_for_customer(Device, user=admin, customer_pk=customer.id)
