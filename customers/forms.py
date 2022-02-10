from django import forms
from django.urls import reverse_lazy

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button, Field
from crispy_forms.bootstrap import FormActions

from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            'name',
            'description'
        )

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.attrs = {
            'hx-post': reverse_lazy('customer_create'),
            'id': 'customer-form',
        }
        self.helper.layout = Layout(
            FormActions(
                Field('name'),
                Field('description'),
                Submit('save', 'Save'),
                Button('cancel', 'Cancel', css_class="btn btn-secondary",
                       onclick="closeModal()")
            ))
