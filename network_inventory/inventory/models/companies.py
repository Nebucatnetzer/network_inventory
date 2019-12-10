from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Owner(Company):
    pass


class Customer(Company):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('customer', args=[str(self.id)])


class DeviceManufacturer(Company):

    class Meta:
        verbose_name_plural = "Device Manufacturers"
