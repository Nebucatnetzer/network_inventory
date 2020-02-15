import django_tables2 as tables

from .models import ConnectedDevice
from .models import Device


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
