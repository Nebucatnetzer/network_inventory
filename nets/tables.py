import django_tables2 as tables

from core.tables import CoreTable

from devices.models import DeviceInNet
from .models import Net


class NetsTable(CoreTable):
    id = tables.Column(visible=False)
    name = tables.Column('Net', linkify=True)
    customer = tables.Column('Customer', linkify=True)

        template_name = 'django_tables2/semantic.html'
    class Meta(CoreTable.Meta):
        model = Net


class NetDetailTable(CoreTable):
    device = tables.Column(linkify=True)
    ip = tables.Column()
    net = tables.Column(visible=False)

        template_name = 'django_tables2/semantic.html'
    class Meta(CoreTable.Meta):
        model = DeviceInNet
