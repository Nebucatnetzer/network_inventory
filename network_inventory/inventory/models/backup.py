from django.db import models
from .calendar import Weekday
from .category import Category
from .computer import Computer
from .notification import Notification
from .software import Software


class BackupMethod(Category):
    description = models.TextField()

    class Meta:
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
    exec_time = models.TimeField()
    exec_day = models.ForeignKey(Weekday, models.SET_NULL, blank=True,
                                 null=True)
    target_device = models.ManyToManyField(Computer, through='TargetDevice')

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('backup', args=[str(self.id)])


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
