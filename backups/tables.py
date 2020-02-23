import django_tables2 as tables

from core.tables import CoreTable

from .models import Backup


class BackupsTable(CoreTable):
    id = tables.Column(visible=False)
    name = tables.Column('Backup', linkify=True)
    computer = tables.Column('Computer', linkify=True)
    target_device = tables.ManyToManyColumn(linkify_item=True)

        template_name = 'django_tables2/semantic.html'
    class Meta(CoreTable.Meta):
        model = Backup
