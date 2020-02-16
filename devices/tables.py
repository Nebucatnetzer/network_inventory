import django_tables2 as tables

from .models import ConnectedDevice
from .models import Device
from .models import Warranty


class DevicesTable(tables.Table):
    id = tables.Column(visible=False)
    name = tables.Column('Device', linkify=True)

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = Device


class ConnectedDevicesTable(tables.Table):
    id = tables.Column(visible=False)
    name = tables.Column('ConnectedDevice', linkify=True)

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = ConnectedDevice


class WarrantiesTable(tables.Table):
    customer = tables.Column(linkify=True)
    device = tables.Column(linkify=True)
    valid_from = tables.Column()
    valid_until = tables.Column()
    warranty_type = tables.Column()

    class Meta:
        template_name = 'django_tables2/semantic.html'
