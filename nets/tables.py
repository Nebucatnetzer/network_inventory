import django_tables2 as tables

from devices.models import DeviceInNet
from .models import Net


class NetsTable(tables.Table):
    id = tables.Column(visible=False)
    name = tables.Column('Net', linkify=True)
    customer = tables.Column('Customer', linkify=True)

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = Net


class NetDetailTable(tables.Table):
    device = tables.Column(linkify=True)
    ip = tables.Column()
    net = tables.Column(visible=False)

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = DeviceInNet
