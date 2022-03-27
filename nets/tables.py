import django_tables2 as tables
from django_tables2.utils import A

from core.tables import CoreTable

from devices.models import DeviceInNet
from .models import Net


class NetsTable(CoreTable):
    id = tables.Column(visible=False)
    name = tables.Column("Net", linkify=True)
    customer = tables.Column("Customer", linkify=True)
    description = tables.Column(
        attrs={"td": {"class": "text-truncate", "style": "max-width: 150px;"}}
    )
    delete = tables.LinkColumn(
        "net_delete",
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
        model = Net


class NetDetailTable(CoreTable):
    device = tables.Column(linkify=True)
    ip = tables.Column()
    net = tables.Column(visible=False)

    class Meta(CoreTable.Meta):
        model = DeviceInNet
