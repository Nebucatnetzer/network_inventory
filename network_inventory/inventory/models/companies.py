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
    description = models.TextField()

    def __str__(self):
        return self.name


class DeviceManufacturer(Company):

    class Meta:
        verbose_name_plural = "Device Manufacturers"
