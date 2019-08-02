import django_tables2 as tables
from .models import Net, Device, Backup
from django_tables2.utils import A

class CustomersTable(tables.Table):
    name = tables.LinkColumn('customer', args=[A('pk')])
    nets = tables.LinkColumn('nets', text='Nets', args=[A('pk')])
    computers = tables.LinkColumn('computers', text='Computers', args=[A('pk')])
    devices = tables.LinkColumn('devices', text='Devices', args=[A('pk')])

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

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = Net


class NetDetailTable(tables.Table):
    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = Net


class BackupDetailTable(tables.Table):
    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = Backup
