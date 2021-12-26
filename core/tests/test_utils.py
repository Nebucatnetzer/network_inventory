from django.http import Http404
from mixer.backend.django import mixer

import pytest

from core import utils

from customers.models import Customer
from devices.models import Device

pytestmark = pytest.mark.django_db


def test_get_object_with_view_permission(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    admin = fixture['admin']
    object = utils.get_object_with_view_permission(
        Customer, user=admin, pk=customer.id)
    assert object == customer


def test_get_object_with_view_permission_device(create_admin_user):
    fixture = create_admin_user()
    customer = fixture['customer']
    admin = fixture['admin']
    device = mixer.blend(Device, customer=customer)
    object = utils.get_object_with_view_permission(
        Device, user=admin, pk=device.id)
    assert object == device


def test_get_object_without_view_permission(create_admin_user):
    fixture = create_admin_user()
    customer = mixer.blend(Customer)
    admin = fixture['admin']
    with pytest.raises(Http404):
        utils.get_object_with_view_permission(
            Customer, user=admin, pk=customer.id)


def test_get_object_without_view_permission_device(create_admin_user):
    fixture = create_admin_user()
    customer = mixer.blend(Customer)
    admin = fixture['admin']
    device = mixer.blend(Device, customer=customer)
    with pytest.raises(Http404):
        utils.get_object_with_view_permission(
            Device, user=admin, pk=device.id)
