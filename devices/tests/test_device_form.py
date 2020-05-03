import pytest
from mixer.backend.django import mixer

from devices import forms

pytestmark = pytest.mark.django_db


def test_device_create_form(create_admin_user):
    fixture = create_admin_user()
    user = mixer.blend("auth.User", customer=fixture['customer'])
    form = forms.DeviceCreateForm(user=user, data={})
    assert form.is_valid() is False, (
        "Should be false because no data was given")

    data = {"name": "pharma-device1",
            "customer": 3}
    form = forms.DeviceCreateForm(user=user, data=data)
    assert form.is_valid() is False, (
        "Should be false because the customer doesn't exist.")

    data = {"name": "pharma-device1",
            "customer": fixture['customer'].id}
    form = forms.DeviceCreateForm(user=fixture['admin'], data=data)
    assert form.is_valid() is True, ("Should be valid with the given data.")


def test_device_update_form(create_admin_user):
    fixture = create_admin_user()
    form = forms.DeviceUpdateForm(data={})
    assert form.is_valid() is False, (
        "Should be false because no data was given")

    data = {"name": "pharma-device1",
            "customer": 3}
    form = forms.DeviceUpdateForm(data=data)
    assert form.is_valid() is False, (
        "Should be false because the customer doesn't exist.")

    data = {"name": "pharma-device1",
            "customer": fixture['customer'].id}
    form = forms.DeviceUpdateForm(data=data)
    assert form.is_valid() is True, ("Should be valid with the given data.")