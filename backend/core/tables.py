import django_tables2 as tables


class CoreTable(tables.Table):

    class Meta:
        attrs = {"class": "table table-hover table-bordered"}
