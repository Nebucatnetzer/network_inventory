import django_tables2 as tables

from core.tables import CoreTable

from .models import ConnectedDevice
from .models import Device
from .models import Warranty


class DevicesTable(CoreTable):
    id = tables.Column(visible=False)
    name = tables.Column('Device', linkify=True)

        template_name = 'django_tables2/semantic.html'
    class Meta(CoreTable.Meta):
        model = Device


class ConnectedDevicesTable(CoreTable):
    id = tables.Column(visible=False)
    name = tables.Column('ConnectedDevice', linkify=True)

        template_name = 'django_tables2/semantic.html'
    class Meta(CoreTable.Meta):
        model = ConnectedDevice


class WarrantiesTable(CoreTable):
    customer = tables.Column(linkify=True, orderable=False)
    device = tables.Column(linkify=True)
    valid_from = tables.Column()
    valid_until = tables.Column()
    warranty_type = tables.Column()

        template_name = 'django_tables2/semantic.html'
    class Meta(CoreTable.Meta):
        pass
