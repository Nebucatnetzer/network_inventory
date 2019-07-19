from django.db import models
from .devices import Device
from .category import Category


class WarrantyType(Category):
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Warranty Types"


class Warranty(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    valid_from = models.DateField()
    valid_until = models.DateField()
    duration_in_years = models.IntegerField()
    warranty_type = models.ForeignKey(WarrantyType, models.SET_NULL,
                                      blank=True, null=True)

    def __str__(self):
        return self.device

    class Meta:
        verbose_name_plural = "Warranties"
