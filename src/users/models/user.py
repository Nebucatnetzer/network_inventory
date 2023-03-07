from django.db import models
from customers.models import Customer


class User(models.Model):
    name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name + " " + self.first_name

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("user", args=[str(self.id)])
