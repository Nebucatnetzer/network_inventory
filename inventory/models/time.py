from django.db import models


class HoursInDay(models.Model):
    name = models.IntegerField()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Hours"
        ordering = ['name']


class MinutesInHour(models.Model):
    name = models.IntegerField()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Minutes"
        ordering = ['name']
