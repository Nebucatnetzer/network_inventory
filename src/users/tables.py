import django_tables2 as tables
from django_tables2.utils import A

from core.tables import CoreTable

from .models import Group
from .models import User


class UsersTable(CoreTable):
    id = tables.Column(visible=False)
    name = tables.Column("User", linkify=True)
    description = tables.Column(
        attrs={"td": {"class": "text-truncate", "style": "max-width: 150px;"}}
    )
    customer = tables.Column("Customer", linkify=True)
    logins = tables.ManyToManyColumn(
        accessor=tables.A("user__login"), verbose_name="Logins"
    )
    groups = tables.ManyToManyColumn(
        accessor=tables.A("group__login__user"), verbose_name="Groups"
    )
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


class GroupsTable(CoreTable):
    id = tables.Column(visible=False)
    name = tables.Column("Groups", linkify=True)
    customer = tables.Column(visible=False)
    action = tables.LinkColumn(
        "group_delete",
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
        model = Group
