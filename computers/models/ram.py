from django.db import models

from core.models import Category


class RamType(Category):

    class Meta:
        verbose_name_plural = "Types of RAM Modules"


class Ram(models.Model):
    ram_type = models.ForeignKey(RamType, on_delete=models.CASCADE)
    size_in_gb = models.IntegerField()
    ecc = models.BooleanField(default=False)

    def __str__(self):
        return '{} {} GB'.format(self.ram_type, self.size_in_gb)

    class Meta:
        verbose_name_plural = "RAM Modules"
