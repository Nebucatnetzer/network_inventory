from django.db import models
from .category import Category
from .companies import Company


class CpuArchitecture(Category):

    class Meta:
        verbose_name_plural = "CPU Architectures"


class CpuManufacturer(Company):

    class Meta:
        verbose_name_plural = "CPU Manufacturers"


class Cpu(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(CpuManufacturer, on_delete=models.CASCADE)
    number_of_cores = models.IntegerField()
    frequency = models.FloatField()
    architecture = models.ForeignKey(CpuArchitecture, on_delete=models.CASCADE)
    hyper_threading = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "CPUs"
