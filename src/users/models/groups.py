from django.db import models

from core.models import Service
from customers.models import Customer


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    mail_address = models.EmailField(blank=True, null=True)
    parent_group = models.ForeignKey(
        "self", blank=True, null=True, on_delete=models.SET_NULL
    )
    service = models.ForeignKey(
        Service, blank=True, null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("group", args=[str(self.id)])
