import pytest
from mixer.backend.django import mixer

from django.http import HttpRequest

from computers import forms

pytestmark = pytest.mark.django_db


def test_computer_create_form(create_admin_user):
    fixture = create_admin_user()
    user = mixer.blend("core.InventoryUser", customer=fixture["customer"])
    form = forms.ComputerCreateForm(user=user, data={})
    assert form.is_valid() is False, "Should be false because no data was given"

    data = {"name": "pharma-pc1", "customer": 3}
    form = forms.ComputerCreateForm(user=user, data=data)
    assert (
        form.is_valid() is False
    ), "Should be false because the customer doesn't exist."

    data = {"name": "pharma-pc1", "customer": fixture["customer"].id}
    form = forms.ComputerCreateForm(user=fixture["admin"], data=data)
    assert form.is_valid() is True, "Should be valid with the given data."


def test_computer_update_form(create_admin_user):
    fixture = create_admin_user()
    request = HttpRequest()
    request.user = fixture["admin"]
    form = forms.ComputerUpdateForm(request, data={})
    assert form.is_valid() is False, "Should be false because no data was given"

    data = {"name": "pharma-pc1", "customer": 20356}
    form = forms.ComputerUpdateForm(request, data=data)
    assert (
        form.is_valid() is False
    ), "Should be false because the customer doesn't exist."

    data = {"name": "pharma-pc1", "customer": fixture["customer"].id}
    form = forms.ComputerUpdateForm(request, data=data)
    assert form.is_valid() is True, "Should be valid with the given data."
