from django.db import models
from .software import SoftwareArchitecture


class OperatingSystem(models.Model):
    name = models.CharField(max_length=50)
    architecture = models.ForeignKey(SoftwareArchitecture, models.SET_NULL,
                                     null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Operating Systems"
