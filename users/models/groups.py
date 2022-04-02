from django.db import models

from customers.models import Customer


class Group(models.Model):
    name = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    mail_address = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("group", args=[str(self.id)])
