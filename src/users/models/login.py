from django.db import models

from core.models import Service

from users.models import User
from users.models import Group


class Login(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True)
    enabled = models.BooleanField()
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(
        Service, on_delete=models.SET_NULL, blank=True, null=True
    )
    groups = models.ManyToManyField(Group, through="LoginInGroup")


class LoginInGroup(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
