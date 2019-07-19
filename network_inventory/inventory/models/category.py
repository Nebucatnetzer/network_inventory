from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
