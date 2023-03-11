from django.db import models
from users.models import Login


class MailAlias(models.Model):
    email_address = models.EmailField()
    login = models.ForeignKey(Login, on_delete=models.CASCADE)

    def __str__(self):
        return self.email_address

    class Meta:
        verbose_name_plural = "Mail Aliases"
