from django.db import models

from customers.models import Customer
from computers.models import Computer
from users.models import User
from softwares.models import Software


class License(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    key = models.CharField(max_length=50, null=True, blank=True)
    software = models.ForeignKey(Software,
                                 null=True,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return str(self.customer) + ": " + str(self.software)

    class Meta:
        abstract = True


class UserLicense(License):
    max_allowed_users = models.IntegerField(null=True, blank=True)
    user = models.ManyToManyField(User, through="LicenseWithUser")

    class Meta:
        ordering = ['software']

    @property
    def used_licenses(self):
        return LicenseWithUser.objects.filter(license=self).count()


class ComputerLicense(License):
    max_allowed_computers = models.IntegerField(null=True, blank=True)
    computer = models.ManyToManyField(Computer, through="LicenseWithComputer")

    class Meta:
        ordering = ['software']

    @property
    def used_licenses(self):
        return LicenseWithComputer.objects.filter(license=self).count()


class LicenseWithUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    license = models.ForeignKey(UserLicense, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'license'],
                                    name='user per license')
        ]


class LicenseWithComputer(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    license = models.ForeignKey(ComputerLicense, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['computer', 'license'],
                                    name='computer per license')
        ]
