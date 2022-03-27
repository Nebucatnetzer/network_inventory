import django_tables2 as tables
from django_tables2.utils import A

from core.tables import CoreTable

from .models import AdGroup
from .models import MailGroup
from .models import User


class UsersTable(CoreTable):
    id = tables.Column(visible=False)
    name = tables.Column("User", linkify=True)
    description = tables.Column(
        attrs={"td": {"class": "text-truncate", "style": "max-width: 150px;"}}
    )
    customer = tables.Column("Customer", linkify=True)
    ad_groups = tables.ManyToManyColumn()
    mail_groups = tables.ManyToManyColumn()
    delete = tables.LinkColumn(
        "user_delete",
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
        model = User


class AdGroupsTable(CoreTable):
    id = tables.Column(visible=False)
    name = tables.Column("Ad Groups", linkify=True)
    customer = tables.Column(visible=False)
    action = tables.LinkColumn(
        "ad_group_delete",
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
        model = AdGroup


class MailGroupsTable(CoreTable):
    id = tables.Column(visible=False)
    name = tables.Column("Mail Groups", linkify=True)
    mail_address = tables.EmailColumn(verbose_name="Mail Address")
    customer = tables.Column(visible=False)
    action = tables.LinkColumn(
        "mail_group_delete",
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
        model = MailGroup
