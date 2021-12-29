import pytest
from mixer.backend.django import mixer

from devices import forms

pytestmark = pytest.mark.django_db


def test_warranty_create_form(create_admin_user):
    create_admin_user()
    form = forms.WarrantyCreateForm(data={})
    assert form.is_valid() is False, (
        "Should be false because no data was given")

    device = mixer.blend("devices.Device")

    data = {"device": device,
            "valid_from": "2010-01-01",
            "valid_until": "2020-01-01"}
    form = forms.WarrantyCreateForm(data=data)
    assert form.is_valid() is True, ("Should be valid with the given data.")

    data = {"device": device,
            "valid_from": "2010-01-01",
            "valid_until": "2000-01-01"}
    form = forms.WarrantyCreateForm(data=data)
    assert form.is_valid() is False, (
        "Should be false because valid from is before valid until")
    assert "Valid from date must be before valid until date" == form.errors[
        "__all__"][0]


def test_warranty_update_form(create_admin_user):
    create_admin_user()
    warranty = mixer.blend("devices.Warranty", valid_from="2010-01-01",
                           valid_until="2020-01-01")
    data = {
        "warranty": warranty,
        "valid_from": "2010-01-01",
        "valid_until": "2000-01-01"
    }
    form = forms.WarrantyUpdateForm(data=data)
    assert form.is_valid() is False
    assert "Valid from date must be before valid until date" == form.errors[
        "__all__"][0]
