from django.urls import reverse_lazy
import floppyforms.__future__ as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Button, Div
from crispy_forms.bootstrap import FormActions

from core import utils

from customers.models import Customer
from customers.models import Location

from devices.models import Device
from devices.models import DeviceCategory
from devices.models import DeviceInNet
from devices.models import Warranty

from users.models import User


class DeviceCategoryForm(forms.ModelForm):
    class Meta:
        model = DeviceCategory
        fields = (
            'name',
        )

    def __init__(self, *args, **kwargs):
        super(DeviceCategoryForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.attrs = {
            'hx-post': reverse_lazy('device_category_create'),
            'id': 'device-category-form',
        }
        self.helper.layout.append(
            FormActions(
                Submit('save_category', 'Save'),
                Button('cancel', 'Cancel', css_class="btn btn-secondary",
                       onclick="closeModal()")
            ))


class DeviceCreateForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = (
            'name',
            'customer',
        )

    def __init__(self, user=None, *args, **kwargs):
        """
        If the user is not a superuser it's always assigned to a customer which
        we can use to assign to the field.
        """
        super(DeviceCreateForm, self).__init__(*args, **kwargs)
        self.fields['customer'].queryset = (
            utils.objects_for_allowed_customers(
                Customer, user=user))


class DeviceUpdateForm(forms.ModelForm):
    """
    Basic form class to use crispies HTML5 forms.
    """

    def __init__(self, request, *args, **kwargs):
        super(DeviceUpdateForm, self).__init__(*args, **kwargs)
        customers = utils.objects_for_allowed_customers(Customer,
                                                        user=request.user)
        locations = utils.objects_for_allowed_customers(Location,
                                                        user=request.user)
        users = utils.objects_for_allowed_customers(User,
                                                    user=request.user)
        self.fields['customer'].queryset = customers
        self.fields['location'].queryset = locations
        self.fields['user'].queryset = users
        self.helper = FormHelper()
        self.helper.form_id = 'htmx-device-form'
        self.helper.layout = Layout(
            'name',
            'customer',
            Div(
                Div('location', id="htmx-location-target"),
                HTML("""
                    <a hx-get="{% url 'htmx_create_location' %}"
                    hx-swap="innerHTML" hx-target="#htmx-modal-position"
                    href=""
                    class="add" title="Add" data-toggle="tooltip"><i
                    class="material-icons">add</i></a>
                """),
                css_class="input-group"),
            'user',
            Div(
                Div('category', id="htmx-category-target"),
                HTML("""
                    <a hx-get="{% url 'device_category_create' %}"
                    hx-swap="innerHTML" hx-target="#htmx-modal-position"
                    href=""
                    class="add" title="Add" data-toggle="tooltip"><i
                    class="material-icons">add</i></a>
                """),
                css_class="input-group"),
            'serialnumber',
            'description',
            FormActions(
                Submit('save_device', 'Save'),
                HTML(
                    """<a href="{{ request.META.HTTP_REFERER }}"
                    class="btn btn-secondary">Cancel</a>""")
            ),
            Div(css_id='htmx-modal-position', css_class="col")
        )

    class Meta:
        model = Device
        fields = '__all__'
        exclude = ('net',)


class WarrantyCreateForm(forms.ModelForm):
    """
    Basic form class to use crispies HTML5 forms.
    """

    def clean(self):
        cleaned_data = super().clean()
        valid_from = cleaned_data.get("valid_from")
        valid_until = cleaned_data.get("valid_until")

        if valid_from and valid_until:
            if valid_from > valid_until:
                raise forms.ValidationError(
                    "Valid from date must be before valid until date")
        return cleaned_data

    class Meta:
        model = Warranty
        fields = '__all__'


class WarrantyUpdateForm(forms.ModelForm):
    """
    Basic form class to use crispies HTML5 forms.
    """

    def clean(self):
        cleaned_data = super().clean()
        valid_from = cleaned_data.get("valid_from")
        valid_until = cleaned_data.get("valid_until")

        if valid_from and valid_until:
            if valid_from > valid_until:
                raise forms.ValidationError(
                    "Valid from date must be before valid until date")
        return cleaned_data

    class Meta:
        model = Warranty
        fields = '__all__'


class DeviceInNetCreateForm(forms.ModelForm):
    """
    Basic form class to use crispies HTML5 forms.
    """
    class Meta:
        model = DeviceInNet
        fields = '__all__'


class DeviceInNetUpdateForm(forms.ModelForm):
    """
    Basic form class to use crispies HTML5 forms.
    """
    class Meta:
        model = DeviceInNet
        fields = '__all__'
