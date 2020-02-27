import floppyforms.__future__ as forms

from .models import Computer


class ComputerCreateForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = (
            'name',
            'customer',
        )


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