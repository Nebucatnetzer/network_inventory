from django.db import models
from customers.models import Customer
from .groups import Group


class User(models.Model):
    name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    ad_login = models.CharField(max_length=50, blank=True)
    ad_pw = models.CharField(max_length=50, blank=True)
    primary_mail = models.CharField(max_length=50, blank=True)
    mail_pw = models.CharField(max_length=50, blank=True)
    enabled = models.BooleanField()
    description = models.TextField(blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, through="UserInGroup")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name + " " + self.first_name

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("user", args=[str(self.id)])


class UserInGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
