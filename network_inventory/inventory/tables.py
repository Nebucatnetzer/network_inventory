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
    name = tables.LinkColumn('computer', args=[A('pk')])
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
    name = tables.LinkColumn('device', args=[A('pk')])

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = Device


class NetsTable(tables.Table):
    name = tables.LinkColumn('net', args=[A('pk')])
    customer = tables.LinkColumn('customer', args=[A('customer.id')])

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = Net


class BackupsTable(tables.Table):
    name = tables.LinkColumn('backup', args=[A('pk')])
    computer = tables.LinkColumn('computer', args=[A('computer.id')])

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = Backup


class NetDetailTable(tables.Table):
    device = tables.LinkColumn('computer', args=[A('pk')])
    ip = tables.Column()
    net = tables.Column(visible=False)

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = DeviceInNet


class BackupDetailTable(tables.Table):
    computer = tables.LinkColumn('computer', args=[A('pk')])

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = Backup
