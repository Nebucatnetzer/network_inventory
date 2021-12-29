import floppyforms.__future__ as forms

from core import utils

from customers.models import Customer

from devices.models import Device
from devices.models import DeviceInNet
from devices.models import Warranty


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
        if not user.is_superuser:
            self.fields['customer'].queryset = (
                utils.get_all_objects_for_allowed_customers(
                    Customer, user=user))


class DeviceUpdateForm(forms.ModelForm):
    """
    Basic form class to use crispies HTML5 forms.
    """
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
