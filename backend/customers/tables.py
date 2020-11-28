import django_tables2 as tables
from django_tables2.utils import A

from core.tables import CoreTable


class CustomersTable(CoreTable):
    name = tables.LinkColumn('customer',
                             args=[A('pk')])
    nets = tables.LinkColumn('nets',
                             text='Nets',
                             args=[A('pk')],
                             orderable=False)
    computers = tables.LinkColumn('computers',
                                  text='Computers',
                                  args=[A('pk')],
                                  orderable=False)
    devices = tables.LinkColumn('devices',
                                text='Devices',
                                args=[A('pk')],
                                orderable=False)
    backups = tables.LinkColumn('backups',
                                text='Backups',
                                args=[A('pk')],
                                orderable=False)
    licenses = tables.LinkColumn('licenses',
                                 text='Licenses',
                                 args=[A('pk')],
                                 orderable=False)
    users = tables.LinkColumn('users',
                              text='Users',
                              args=[A('pk')],
                              orderable=False)
    delete = tables.LinkColumn('customer_delete',
                               text='delete',
                               args=[A('pk')], attrs={
                                   'a': {'class': 'delete material-icons', }
                               }, orderable=False)

    class Meta(CoreTable.Meta):
        pass
