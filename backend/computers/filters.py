from django_filters import FilterSet

from .models import Computer


class ComputerFilter(FilterSet):
    class Meta:
        model = Computer
        fields = {"name": ["contains"], "customer": ["exact"]}
