from django.db import models
from .category import Category


class SoftwareArchitecture(Category):

    class Meta:
        verbose_name_plural = "Software Architectures"


class SoftwareCategory(Category):

    class Meta:
        verbose_name_plural = "Software Categories"


class Software(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(SoftwareCategory, models.SET_NULL, null=True,
                                blank=True)

    def __str__(self):
        return self.name

