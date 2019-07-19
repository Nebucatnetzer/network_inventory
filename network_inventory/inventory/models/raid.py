from django.db import models
from .disk import Disk
from .category import Category


class RaidType(Category):
    pass


class DisksInRaid(models.Model):
    raid = models.ForeignKey(RaidType, on_delete=models.CASCADE)
    disk = models.ForeignKey(Disk, on_delete=models.CASCADE)
    disk_amount = models.IntegerField()
