from django.contrib.auth.models import AbstractUser


class InventoryUser(AbstractUser):
    def __str__(self):
        if self.first_name and self.last_name:
            return self.first_name + " " + self.last_name
        return self.username
