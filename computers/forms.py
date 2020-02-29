import floppyforms.__future__ as forms

from core import utils

from computers.models import Computer


class ComputerCreateForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = (
            'name',
            'customer',
        )

    def __init__(self, user=None, *args, **kwargs):
        super(ComputerCreateForm, self).__init__(*args, **kwargs)
        if not user.is_superuser:
            self.fields['customer'].queryset = utils.get_customers(user)


class ComputerUpdateForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = (
            'name',
            'description',
            'serialnumber',
            'category',
            'owner',
            'customer',
            'manufacturer',
            'model',
            'location',
            'user',
            'installation_date',
        )

    def __init__(self, user=None, *args, **kwargs):
        super(ComputerUpdateForm, self).__init__(*args, **kwargs)
        if not user.is_superuser:
            self.fields['customer'].queryset = utils.get_customers(user)
            self.fields['user'].queryset = utils.get_objects("User", user)