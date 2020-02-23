import django_tables2 as tables

from core.tables import CoreTable

from .models import User


class UsersTable(CoreTable):
    id = tables.Column(visible=False)
    name = tables.Column('User', linkify=True)
    customer = tables.Column('Customer', linkify=True)
    ad_groups = tables.ManyToManyColumn()
    mail_groups = tables.ManyToManyColumn()

        template_name = 'django_tables2/semantic.html'
    class Meta(CoreTable.Meta):
        model = User
