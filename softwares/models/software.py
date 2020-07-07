from django.db import models

from core.models import Category


class SoftwareArchitecture(Category):

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Software Architectures"


class SoftwareCategory(Category):

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Software Categories"


class Software(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(SoftwareCategory, models.SET_NULL, null=True,
                                 blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
