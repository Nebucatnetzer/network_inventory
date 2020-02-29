from datetime import datetime, timedelta

import django_tables2 as tables

from core.tables import CoreTable

from .models import ConnectedDevice
from .models import Device


class DevicesTable(CoreTable):
    id = tables.Column(visible=False)
    name = tables.Column('Device', linkify=True)

    class Meta(CoreTable.Meta):
        model = Device


class ConnectedDevicesTable(CoreTable):
    id = tables.Column(visible=False)
    name = tables.Column('ConnectedDevice', linkify=True)

    class Meta(CoreTable.Meta):
        model = ConnectedDevice


class WarrantiesTable(CoreTable):
    customer = tables.Column(linkify=True, orderable=False)
    device = tables.Column(linkify=True)
    valid_from = tables.Column()
    valid_until = tables.Column()
    warranty_type = tables.Column()

    class Meta(CoreTable.Meta):
        pass

    def render_valid_until(self, value, column):
        today = datetime.date(datetime.today())
        one_year_from_today = (datetime.date(datetime.today() + timedelta(365)))

        if value > one_year_from_today:
            column.attrs = {'td': {}}
            return value
        if value <= today:
            column.attrs = {'td': {'bgcolor': 'red'}}
            return value
        if value <= one_year_from_today:
            column.attrs = {'td': {'bgcolor': 'orange'}}
            return value
