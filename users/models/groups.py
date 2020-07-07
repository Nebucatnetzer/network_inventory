from django.db import models
from customers.models import Customer


class Group(models.Model):
    name = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class AdGroup(Group):

    class Meta:
        ordering = ['name']
        verbose_name_plural = "AD Groups"


class MailGroup(Group):
    mail_address = models.EmailField()

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Mail Groups"
