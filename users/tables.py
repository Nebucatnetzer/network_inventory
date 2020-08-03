import django_tables2 as tables
from django_tables2.utils import A

from core.tables import CoreTable

from .models import User


class UsersTable(CoreTable):
    id = tables.Column(visible=False)
    name = tables.Column('User', linkify=True)
    customer = tables.Column('Customer', linkify=True)
    ad_groups = tables.ManyToManyColumn()
    mail_groups = tables.ManyToManyColumn()
    delete = tables.LinkColumn('user_delete',
                               text='delete',
                               args=[A('pk')], attrs={
                                   'a': {'class': 'delete material-icons', }
                               }, orderable=False)

    class Meta(CoreTable.Meta):
        model = User
