from django.db import models
from .category import Category
from .companies import Customer


class IpStatus(Category):

    class Meta:
        verbose_name_plural = "IP Status"


class Net(models.Model):
    name = models.CharField(max_length=50)
    ip_range = models.CharField(max_length=50)
    dhcp_range = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
