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
                utils.get_all_objects_for_alLowed_customers(
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
    class Meta:
        model = Warranty
        fields = '__all__'


class WarrantyUpdateForm(forms.ModelForm):
    """
    Basic form class to use crispies HTML5 forms.
    """
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
