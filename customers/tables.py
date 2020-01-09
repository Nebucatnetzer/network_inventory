import django_tables2 as tables
from django_tables2.utils import A


class CustomersTable(tables.Table):
    name = tables.LinkColumn('customer', args=[A('pk')])
    nets = tables.LinkColumn('nets', text='Nets', args=[A('pk')],
                             orderable=False)
    computers = tables.LinkColumn('computers', text='Computers', args=[A('pk')],
                                  orderable=False)
    devices = tables.LinkColumn('devices', text='Devices', args=[A('pk')],
                                orderable=False)
    backups = tables.LinkColumn('backups', text='Backups', args=[A('pk')],
                                orderable=False)
    licenses = tables.LinkColumn('licenses', text='Licenses', args=[A('pk')],
                                 orderable=False)
    users = tables.LinkColumn('users', text='Users', args=[A('pk')],
                              orderable=False)

    class Meta:
        template_name = 'django_tables2/semantic.html'
