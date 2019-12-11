import django_tables2 as tables
from .models import Net, Device, Backup, DeviceInNet
from django_tables2.utils import A


class CustomersTable(tables.Table):
    name = tables.LinkColumn('customer', args=[A('pk')])
    nets = tables.LinkColumn('nets', text='Nets', args=[A('pk')])
    computers = tables.LinkColumn('computers', text='Computers', args=[A('pk')])
    devices = tables.LinkColumn('devices', text='Devices', args=[A('pk')])
    backups = tables.LinkColumn('backups', text='Backups', args=[A('pk')])

    class Meta:
        template_name = 'django_tables2/semantic.html'


class ComputersTable(tables.Table):
    name = tables.Column('computer', linkify=True)
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
    name = tables.Column('device', linkify=True)

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = Device


class NetsTable(tables.Table):
    name = tables.Column('net', linkify=True)
    customer = tables.Column('customer', linkify=True)

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = Net


class BackupsTable(tables.Table):
    name = tables.Column('backup', linkify=True)
    computer = tables.Column('computer', linkify=True)

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = Backup


class NetDetailTable(tables.Table):
    device = tables.Column('computer', linkify=True)
    ip = tables.Column()
    net = tables.Column(visible=False)

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = DeviceInNet


class BackupDetailTable(tables.Table):
    computer = tables.Column('computer', linkify=True)

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = Backup
