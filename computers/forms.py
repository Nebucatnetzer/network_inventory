import floppyforms.__future__ as forms

from core import utils

from computers.models import Computer
from computers.models import ComputerCpuRelation
from computers.models import ComputerRamRelation
from devices.models import Warranty


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

    # def __init__(self, user=None, *args, **kwargs):
    #     super(ComputerUpdateForm, self).__init__(*args, **kwargs)
    #     if not user.is_superuser:
    #         self.fields['customer'].queryset = utils.get_customers(user)
    #         self.fields['user'].queryset = utils.get_objects("User", user)


ComputerFormSet = forms.inlineformset_factory(Computer,
                                              Warranty,
                                              fields=(
                                                   'valid_from',
                                                   'valid_until',
                                                   'warranty_type',
                                               ),
                                              exclude=[],
                                              can_delete=False,
                                              form=ComputerUpdateForm,
                                              max_num=1)


CpuFormSet = forms.inlineformset_factory(Computer,
                                         ComputerCpuRelation,
                                         fields=(
                                             'cpu',
                                             'computer',
                                             'amount',
                                             ),
                                         exclude=[],
                                         can_delete=False,
                                         form=ComputerUpdateForm,
                                         max_num=1)


RamFormSet = forms.inlineformset_factory(Computer,
                                         ComputerRamRelation,
                                         fields=(
                                             'ram',
                                             'computer',
                                             'amount',
                                             ),
                                         exclude=[],
                                         can_delete=False,
                                         form=ComputerUpdateForm,
                                         max_num=1)
