from django import forms
from django.urls import reverse_lazy

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from crispy_forms.bootstrap import FormActions

from core import utils
from .models import Customer, DummyLocation, Location


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            'name',
            'description'
        )

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.attrs = {
            'hx-post': reverse_lazy('customer_create'),
            'id': 'customer-form',
        }
        self.helper.layout.append(
            FormActions(
                Submit('save', 'Save'),
                Button('cancel', 'Cancel', css_class="btn btn-secondary",
                       onclick="closeModal()")
            ))


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = (
            'name',
            'customer'
        )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super(LocationForm, self).__init__(*args, **kwargs)
        """
        If the user is not a superuser it's always assigned to a customer which
        we can use to assign to the field.
        """
        self.fields['customer'].queryset = (
            utils.objects_for_allowed_customers(
                Customer, user=user))

        self.helper = FormHelper(self)
        self.helper.attrs = {
            'hx-post': reverse_lazy('htmx_create_location'),
            'id': 'location-form',
        }
        self.helper.layout.append(
            FormActions(
                Submit('save_location', 'Save'),
                Button('cancel', 'Cancel', css_class="btn btn-secondary",
                       onclick="closeModal()")
            ))


class DummyLocationForm(forms.ModelForm):
    class Meta:
        model = DummyLocation
        fields = (
            'location',
        )
