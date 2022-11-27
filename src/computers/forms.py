import floppyforms.__future__ as forms

from core import utils

from computers.models import Computer
from computers.models import ComputerCpuRelation
from computers.models import ComputerDiskRelation
from computers.models import ComputerGpuRelation
from computers.models import ComputerRamRelation
from computers.models import ComputerSoftwareRelation
from computers.models import Raid

from customers.models import Customer
from customers.models import Location

from users.models import User


class ComputerCreateForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = (
            "name",
            "customer",
        )

    def __init__(self, user=None, *args, **kwargs):
        """
        If the user is not a superuser it's always assigned to a customer which
        we can use to assign to the field.
        """
        super(ComputerCreateForm, self).__init__(*args, **kwargs)
        customers = utils.objects_for_allowed_customers(Customer, user=user)
        self.fields["customer"].queryset = customers


class ComputerUpdateForm(forms.ModelForm):
    """
    Basic form class to use crispies HTML5 forms.
    """

    def __init__(self, request, *args, **kwargs):
        super(ComputerUpdateForm, self).__init__(*args, **kwargs)
        customers = utils.objects_for_allowed_customers(
            Customer, user=request.user
        )
        locations = utils.objects_for_allowed_customers(
            Location, user=request.user
        )
        hosts = utils.objects_for_allowed_customers(
            Computer, user=request.user
        )
        users = utils.objects_for_allowed_customers(User, user=request.user)
        self.fields["customer"].queryset = customers
        self.fields["location"].queryset = locations
        self.fields["host"].queryset = hosts
        self.fields["user"].queryset = users

    class Meta:
        model = Computer
        fields = "__all__"
        exclude = ("net", "cpu", "ram", "gpu", "disks", "software")


class ComputerRamRelationCreateForm(forms.ModelForm):
    """
    Basic form class to use crispies HTML5 forms.
    """

    class Meta:
        model = ComputerRamRelation
        fields = "__all__"


class ComputerCpuRelationCreateForm(forms.ModelForm):
    """
    Basic form class to use crispies HTML5 forms.
    """

    class Meta:
        model = ComputerCpuRelation
        fields = "__all__"


class ComputerGpuRelationCreateForm(forms.ModelForm):
    """
    Basic form class to use crispies HTML5 forms.
    """

    class Meta:
        model = ComputerGpuRelation
        fields = "__all__"


class ComputerDiskRelationCreateForm(forms.ModelForm):
    """
    Basic form class to use crispies HTML5 forms.
    """

    class Meta:
        model = ComputerDiskRelation
        fields = "__all__"


class ComputerSoftwareRelationCreateForm(forms.ModelForm):
    """
    Basic form class to use crispies HTML5 forms.
    """

    class Meta:
        model = ComputerSoftwareRelation
        fields = "__all__"


class RaidCreateForm(forms.ModelForm):
    """
    Basic form class to use crispies HTML5 forms.
    """

    class Meta:
        model = Raid
        fields = "__all__"
