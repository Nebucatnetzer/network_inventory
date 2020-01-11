import django_tables2 as tables

from .models import Backup


class BackupsTable(tables.Table):
    id = tables.Column(visible=False)
    name = tables.Column('Backup', linkify=True)
    computer = tables.Column('Computer', linkify=True)
    target_device = tables.ManyToManyColumn(linkify_item=True)

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = Backup
