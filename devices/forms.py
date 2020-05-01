import floppyforms.__future__ as forms

from core import utils

from devices.models import Device
from devices.models import Warranty


class DeviceCreateForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = (
            'name',
            'customer',
        )

    def __init__(self, user=None, *args, **kwargs):
        super(DeviceCreateForm, self).__init__(*args, **kwargs)
        if not user.is_superuser:
            self.fields['customer'].queryset = utils.get_customers(user)


class DeviceUpdateForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'


WarrantyFormSet = forms.inlineformset_factory(Device,
                                              Warranty,
                                              fields=(
                                                   'valid_from',
                                                   'valid_until',
                                                   'warranty_type',
                                               ),
                                              exclude=[],
                                              can_delete=False,
                                              form=DeviceUpdateForm,
                                              max_num=1)
