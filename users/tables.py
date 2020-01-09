import django_tables2 as tables

from .models import User


class UsersTable(tables.Table):
    id = tables.Column(visible=False)
    name = tables.Column('User', linkify=True)
    customer = tables.Column('Customer', linkify=True)
    ad_groups = tables.ManyToManyColumn()
    mail_groups = tables.ManyToManyColumn()

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = User
