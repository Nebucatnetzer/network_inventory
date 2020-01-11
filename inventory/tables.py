import django_tables2 as tables

from .models import ComputerLicense
from .models import UserLicense


class ComputersTable(tables.Table):
    name = tables.Column('Computer', linkify=True)
    description = tables.Column()
    serialnumber = tables.Column()
    owner = tables.Column()
    manufacturer = tables.Column()
    location = tables.Column()
    user = tables.Column('User', linkify=True)
    installation_date = tables.Column()
    os = tables.Column()

    class Meta:
        template_name = 'django_tables2/semantic.html'


class UserLicensesTable(tables.Table):
    id = tables.Column(visible=False)
    license_ptr = tables.Column(visible=False)
    customer = tables.Column('Customer', linkify=True)
    used_licenses = tables.Column()
    user = tables.ManyToManyColumn(linkify_item=True)

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = UserLicense


class ComputerLicensesTable(tables.Table):
    id = tables.Column(visible=False)
    license_ptr = tables.Column(visible=False)
    customer = tables.Column('Customer', linkify=True)
    used_licenses = tables.Column()
    computer = tables.ManyToManyColumn(linkify_item=True)

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = ComputerLicense
