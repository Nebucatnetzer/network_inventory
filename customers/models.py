from django.db import models
from core.models import Company


class Owner(Company):
    pass


class Customer(Company):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('customer', args=[str(self.id)])


class DeviceManufacturer(Company):

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Device Manufacturers"


class Location(models.Model):
    name = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
