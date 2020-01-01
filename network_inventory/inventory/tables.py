import django_tables2 as tables
from django_tables2.utils import A

from .models import Backup
from .models import ComputerLicense
from .models import Device
from .models import DeviceInNet
from .models import Net
from .models import User
from .models import UserLicense


class CustomersTable(tables.Table):
    name = tables.LinkColumn('customer', args=[A('pk')])
    nets = tables.LinkColumn('nets', text='Nets', args=[A('pk')],
                             orderable=False)
    computers = tables.LinkColumn('computers', text='Computers', args=[A('pk')],
                                  orderable=False)
    devices = tables.LinkColumn('devices', text='Devices', args=[A('pk')],
                                orderable=False)
    backups = tables.LinkColumn('backups', text='Backups', args=[A('pk')],
                                orderable=False)
    licenses = tables.LinkColumn('licenses', text='Licenses', args=[A('pk')],
                                 orderable=False)
    users = tables.LinkColumn('users', text='Users', args=[A('pk')],
                              orderable=False)

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
    name = tables.Column('Net', linkify=True)
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
    user = tables.ManyToManyColumn()

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


class UsersTable(tables.Table):
    id = tables.Column(visible=False)
    customer = tables.Column('Customer', linkify=True)
    ad_groups = tables.ManyToManyColumn()
    mail_groups = tables.ManyToManyColumn()

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = User
