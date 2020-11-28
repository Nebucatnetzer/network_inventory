from datetime import datetime, timedelta

import django_tables2 as tables
from django_tables2.utils import A

from core.tables import CoreTable

from .models import Device


class DevicesTable(CoreTable):
    id = tables.Column(visible=False)
    name = tables.Column('Device', linkify=True)
    description = tables.Column(
        attrs={
            'td': {
                'class': 'text-truncate',
                'style': 'max-width: 150px;'}
        }
    )
    delete = tables.LinkColumn('device_delete',
                               text='delete',
                               args=[A('pk')], attrs={
                                   'a': {'class': 'delete material-icons', }
                               }, orderable=False)

    class Meta(CoreTable.Meta):
        model = Device


class WarrantiesTable(CoreTable):
    customer = tables.Column(linkify=True, orderable=False)
    device = tables.Column(linkify=True)
    valid_from = tables.Column()
    valid_until = tables.Column()
    warranty_type = tables.Column()
    delete = tables.LinkColumn('warranty_delete',
                               text='delete',
                               args=[A('pk')], attrs={
                                   'a': {'class': 'delete material-icons', }
                               }, orderable=False)

    class Meta(CoreTable.Meta):
        pass

    def render_valid_until(self, value, column):
        today = datetime.date(datetime.today())
        one_year_from_today = (datetime.date(datetime.today()
                                             + timedelta(365)))

        if value > one_year_from_today:
            column.attrs = {'td': {}}
            return value
        if value <= today:
            column.attrs = {'td': {'bgcolor': 'red'}}
            return value
        if value <= one_year_from_today:
            column.attrs = {'td': {'bgcolor': 'orange'}}
            return value
