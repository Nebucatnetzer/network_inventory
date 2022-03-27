import django_tables2 as tables
from django_tables2.utils import A

from core.tables import CoreTable

from .models import Backup


class BackupsTable(CoreTable):
    id = tables.Column(visible=False)
    name = tables.Column("Backup", linkify=True)
    computer = tables.Column("Computer", linkify=True)
    target_device = tables.ManyToManyColumn(linkify_item=True)
    delete = tables.LinkColumn(
        "backup_delete_from-table",
        text="delete",
        args=[A("pk")],
        attrs={
            "a": {
                "class": "delete material-icons",
            }
        },
        orderable=False,
    )

    class Meta(CoreTable.Meta):
        model = Backup
