import django_tables2 as tables

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

    class Meta(CoreTable.Meta):
        pass
