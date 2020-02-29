import floppyforms.__future__ as forms

from guardian.shortcuts import get_objects_for_user

from .models import Computer
from customers.models import Customer
from users.models import User


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

    def __init__(self, user=None, *args, **kwargs):
        super(ComputerUpdateForm, self).__init__(*args, **kwargs)
        if not user.is_superuser:
            customers = get_objects_for_user(user,
                                             'customers.view_customer',
                                             klass=Customer)

            self.fields['customer'].queryset = customers
            self.fields['user'].queryset = User.objects.filter(
                customer__in=customers)
