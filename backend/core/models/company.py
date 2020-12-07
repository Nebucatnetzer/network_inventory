from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name
