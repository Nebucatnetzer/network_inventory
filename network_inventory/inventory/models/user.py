from django.db import models
from .companies import Customer
from .groups import AdGroup, MailGroup


class User(models.Model):
    name = models.CharField(max_length=50)
    ad_login = models.CharField(max_length=50, blank=True)
    ad_pw = models.CharField(max_length=50, blank=True)
    primary_mail = models.CharField(max_length=50, blank=True)
    mail_pw = models.CharField(max_length=50, blank=True)
    enabled = models.BooleanField()
    description = models.TextField(blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ad_groups = models.ManyToManyField(AdGroup, through='UserInAdGroup')
    mail_groups = models.ManyToManyField(MailGroup, through='UserInMailGroup')

    def __str__(self):
        return self.name


class UserInAdGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(AdGroup, on_delete=models.CASCADE)


class UserInMailGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(MailGroup, on_delete=models.CASCADE)
