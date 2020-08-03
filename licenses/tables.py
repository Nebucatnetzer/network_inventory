import django_tables2 as tables
from django_tables2.utils import A

from core.tables import CoreTable

from .models import ComputerLicense
from .models import UserLicense


class UserLicensesTable(CoreTable):
    id = tables.Column(visible=False)
    license_ptr = tables.Column(visible=False)
    customer = tables.Column('Customer', linkify=True)
    used_licenses = tables.Column()
    user = tables.ManyToManyColumn(linkify_item=True)
    delete = tables.LinkColumn('user_license_delete',
                               text='delete',
                               args=[A('pk')], attrs={
                                   'a': {'class': 'delete material-icons', }
                               }, orderable=False)

    class Meta(CoreTable.Meta):
        model = UserLicense


class ComputerLicensesTable(CoreTable):
    id = tables.Column(visible=False)
    license_ptr = tables.Column(visible=False)
    customer = tables.Column('Customer', linkify=True)
    used_licenses = tables.Column()
    computer = tables.ManyToManyColumn(linkify_item=True)
    delete = tables.LinkColumn('computer_license_delete',
                               text='delete',
                               args=[A('pk')], attrs={
                                   'a': {'class': 'delete material-icons', }
                               }, orderable=False)

    class Meta(CoreTable.Meta):
        model = ComputerLicense
