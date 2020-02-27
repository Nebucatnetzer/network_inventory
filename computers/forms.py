import floppyforms.__future__ as forms

from .models import Computer


class ComputerCreateForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = (
            'name',
            'customer',
        )


