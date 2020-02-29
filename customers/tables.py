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
    connected_devices = tables.LinkColumn('connected_devices',
                                          text='Connected Devices',
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

    class Meta(CoreTable.Meta):
        pass
