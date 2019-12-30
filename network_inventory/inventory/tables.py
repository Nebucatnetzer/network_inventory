import django_tables2 as tables
from .models import Net, Device, Backup, DeviceInNet, ComputerLicense, UserLicense
from django_tables2.utils import A


class CustomersTable(tables.Table):
    name = tables.LinkColumn('customer', args=[A('pk')])
    nets = tables.LinkColumn('nets', text='Nets', args=[A('pk')])
    computers = tables.LinkColumn('computers', text='Computers', args=[A('pk')])
    devices = tables.LinkColumn('devices', text='Devices', args=[A('pk')])
    backups = tables.LinkColumn('backups', text='Backups', args=[A('pk')])
    licenses = tables.LinkColumn('licenses', text='Licenses', args=[A('pk')])
    users = tables.LinkColumn('users', text='Users', args=[A('pk')])

    class Meta:
        template_name = 'django_tables2/semantic.html'


class ComputersTable(tables.Table):
    name = tables.Column('Computer', linkify=True)
    description = tables.Column()
    serialnumber = tables.Column()
    owner = tables.Column()
    manufacturer = tables.Column()
    location = tables.Column()
    user = tables.Column()
    installation_date = tables.Column()
    os = tables.Column()

    class Meta:
        template_name = 'django_tables2/semantic.html'


class DevicesTable(tables.Table):
    id = tables.Column(visible=False)
    name = tables.Column('Device', linkify=True)

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = Device


class NetsTable(tables.Table):
    id = tables.Column(visible=False)
    name = tables.Column('net', linkify=True)
    customer = tables.Column('Customer', linkify=True)

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = Net


class BackupsTable(tables.Table):
    id = tables.Column(visible=False)
    name = tables.Column('Backup', linkify=True)
    computer = tables.Column('Computer', linkify=True)
    target_device = tables.ManyToManyColumn(linkify_item=True)

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = Backup


class NetDetailTable(tables.Table):
    device = tables.Column('Computer', linkify=True)
    ip = tables.Column()
    net = tables.Column(visible=False)

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = DeviceInNet


class UserLicensesTable(tables.Table):
    id = tables.Column(visible=False)
    license_ptr = tables.Column(visible=False)
    customer = tables.Column('Customer', linkify=True)
    used_licenses = tables.Column()

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = UserLicense


class ComputerLicensesTable(tables.Table):
    id = tables.Column(visible=False)
    license_ptr = tables.Column(visible=False)
    customer = tables.Column('Customer', linkify=True)
    used_licenses = tables.Column()

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = ComputerLicense
