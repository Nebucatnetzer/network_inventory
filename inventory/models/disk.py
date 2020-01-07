from django.db import models

from core.models import Category


class DiskType(Category):

    class Meta:
        verbose_name_plural = "Types of Disks"
        ordering = ['name']


class Disk(models.Model):
    disk_type = models.ForeignKey(DiskType, on_delete=models.CASCADE)
    size_in_gb = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.disk_type, str(self.size_in_gb) + " GB")

    class Meta:
        ordering = ['disk_type']
