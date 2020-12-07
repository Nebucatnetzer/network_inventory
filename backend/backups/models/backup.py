from django.db import models

from core.models import Category, Weekday
from computers.models import Computer
from softwares.models import Software

from .notification import Notification


class BackupMethod(Category):
    description = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Backup Methods"


class Backup(models.Model):
    name = models.CharField(max_length=50)
    computer = models.ForeignKey(Computer, related_name='source_computer',
                                 on_delete=models.CASCADE)
    method = models.ForeignKey(BackupMethod, models.SET_NULL, blank=True,
                               null=True)
    software = models.ForeignKey(Software, models.SET_NULL, blank=True,
                                 null=True)
    source_path = models.CharField(max_length=200, blank=True)
    exec_time = models.TimeField(null=True, blank=True)
    exec_days = models.ManyToManyField(Weekday, blank=True)
    target_device = models.ManyToManyField(Computer, through='TargetDevice',
                                           blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('backup', args=[str(self.id)])

    @property
    def customer(self):
        return self.computer.customer


class TargetDevice(models.Model):
    device = models.ForeignKey(Computer, models.SET_NULL, blank=True,
                               null=True)
    backup = models.ForeignKey(Backup, on_delete=models.CASCADE)
    target_path = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.device)

    class Meta:
        verbose_name_plural = "Target Devices"


class NotificationFromBackup(models.Model):
    backup = models.ForeignKey(Backup, on_delete=models.CASCADE)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
