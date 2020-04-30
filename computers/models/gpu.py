from django.db import models
from core.models import Company


class GpuManufacturer(Company):

    class Meta:
        verbose_name_plural = "GPU Manufacturers"


class Gpu(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(GpuManufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "GPUs"
