import floppyforms.__future__ as forms

from .models import Computer
from customers.models import Customer


class ComputerCreateForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = (
            'name',
            'customer',
        )

    def __init__(self, pk=None, user=None, *args, **kwargs):
        super(ComputerCreateForm, self).__init__(*args, **kwargs)
        if not user.is_superuser:
            self.fields['customer'].queryset = (Customer.objects.filter(id=pk))


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