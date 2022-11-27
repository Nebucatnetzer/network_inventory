import pytest
from mixer.backend.django import mixer

from customers import forms

pytestmark = pytest.mark.django_db


def test_location_form(create_admin_user):
    fixture = create_admin_user()
    user = fixture["admin"]
    form = forms.LocationForm(user=user, data={})
    assert (
        form.is_valid() is False
    ), "Should be false because no data was given"

    data = {"name": "Main Office", "customer": 3}
    form = forms.LocationForm(user=user, data=data)
    assert (
        form.is_valid() is False
    ), "Should be false because the customer doesn't exist."

    data = {
        "name": mixer.blend("customers.Location").name,
        "customer": fixture["customer"].id,
    }
    form = forms.LocationForm(user=user, data=data)
    assert form.is_valid() is True, "Should be valid with the given data."
