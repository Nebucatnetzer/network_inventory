import django_tables2 as tables
from django_tables2.utils import A

from core.tables import CoreTable


class ComputersTable(CoreTable):
    name = tables.Column('Computer', linkify=True)
    description = tables.Column()
    serialnumber = tables.Column()
    owner = tables.Column()
    manufacturer = tables.Column()
    model = tables.Column()
    location = tables.Column()
    user = tables.Column('User', linkify=True)
    installation_date = tables.Column()
    os = tables.Column()
    delete = tables.LinkColumn('device_delete',
                               text='delete',
                               args=[A('pk')], attrs={
                                   'a': {'class': 'delete material-icons', }
                               }, orderable=False)

    class Meta(CoreTable.Meta):
        pass
