from django.db import models

from core.models import Category

from .disk import Disk
from .computer import Computer


class RaidType(Category):
    pass


class Raid(models.Model):
    usable_space = models.IntegerField(blank=True, null=True)
    raid_type = models.ForeignKey(RaidType, models.SET_NULL, blank=True,
                                  null=True)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.computer)

    class Meta:
        verbose_name_plural = "RAIDs in Computer"


class DisksInRaid(models.Model):
    disk = models.ForeignKey(Disk, on_delete=models.CASCADE)
    disk_amount = models.IntegerField()
    raid = models.ForeignKey(Raid, on_delete=models.CASCADE)
