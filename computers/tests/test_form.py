import pytest

from computers import forms

pytestmark = pytest.mark.django_db


def test_computer_create_form(create_admin_user):
    fixture = create_admin_user()
    form = forms.ComputerCreateForm(user=fixture['admin'], data={})
    assert form.is_valid() is False, (
        "Should be false because no data was given")

    data = {"name": "novartis-pc1",
            "customer": 3}
    form = forms.ComputerCreateForm(user=fixture['admin'], data=data)
    assert form.is_valid() is False, (
        "Should be false because the customer doesn't exist.")

    data = {"name": "novartis-pc1",
            "customer": fixture['customer'].id}
    form = forms.ComputerCreateForm(user=fixture['admin'], data=data)
    assert form.is_valid() is True, ("Should be valid with the given data.")


def test_computer_update_form(create_admin_user):
    fixture = create_admin_user()
    form = forms.ComputerUpdateForm(user=fixture['admin'], data={})
    assert form.is_valid() is False, (
        "Should be false because no data was given")

    data = {"name": "novartis-pc1",
            "customer": 3}
    form = forms.ComputerUpdateForm(user=fixture['admin'], data=data)
    assert form.is_valid() is False, (
        "Should be false because the customer doesn't exist.")

    data = {"name": "novartis-pc1",
            "customer": fixture['customer'].id}
    form = forms.ComputerUpdateForm(user=fixture['admin'], data=data)
    assert form.is_valid() is True, ("Should be valid with the given data.")
