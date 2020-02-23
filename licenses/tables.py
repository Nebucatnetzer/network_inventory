import django_tables2 as tables

from core.tables import CoreTable

from .models import ComputerLicense
from .models import UserLicense


class UserLicensesTable(CoreTable):
    id = tables.Column(visible=False)
    license_ptr = tables.Column(visible=False)
    customer = tables.Column('Customer', linkify=True)
    used_licenses = tables.Column()
    user = tables.ManyToManyColumn(linkify_item=True)

    class Meta(CoreTable.Meta):
        model = UserLicense


class ComputerLicensesTable(CoreTable):
    id = tables.Column(visible=False)
    license_ptr = tables.Column(visible=False)
    customer = tables.Column('Customer', linkify=True)
    used_licenses = tables.Column()
    computer = tables.ManyToManyColumn(linkify_item=True)

    class Meta(CoreTable.Meta):
        model = ComputerLicense
