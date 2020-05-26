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
        """
        If the user is not a superuser it's always assigned to a customer which
        we can use to assign to the field.
        """
        super(ComputerCreateForm, self).__init__(*args, **kwargs)
        if not user.is_superuser:
            self.fields['customer'].queryset = utils.get_customers(user)


class ComputerUpdateForm(forms.ModelForm):
    """
    Basic form class to use crispies HTML5 forms.
    """
    class Meta:
        model = Computer
        fields = '__all__'
        exclude = ('net', 'cpu', 'ram', 'gpu', 'disks', 'software')
