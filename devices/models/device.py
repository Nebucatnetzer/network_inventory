from django.core.validators import RegexValidator
from django.db import models
from core.models import Category, Company
from customers.models import Customer, Owner, Location
from users.models import User
from nets.models import Net, IpStatus


class DeviceManufacturer(Company):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17,
                                    blank=True, null=True)
    email_address = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Device Manufacturers"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('manufacturer', args=[str(self.id)])


class DeviceCategory(Category):

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Device Categories"


class HardwareModel(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(DeviceManufacturer,
                                     on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    serialnumber = models.CharField(max_length=50, blank=True)
    category = models.ForeignKey(DeviceCategory,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)
    owner = models.ForeignKey(Owner,
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(DeviceManufacturer,
                                     models.SET_NULL,
                                     null=True,
                                     blank=True)
    model = models.ForeignKey(HardwareModel,
                              models.SET_NULL,
                              null=True,
                              blank=True)
    location = models.ForeignKey(Location,
                                 models.SET_NULL,
                                 null=True,
                                 blank=True)
    user = models.ForeignKey(User,
                             models.SET_NULL,
                             null=True,
                             blank=True)
    installation_date = models.DateField(null=True, blank=True)
    net = models.ManyToManyField(Net, through='DeviceInNet')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('device', args=[str(self.id)])


class DeviceInNet(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    net = models.ForeignKey(Net, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField(verbose_name="IP", blank=True, null=True)
    nic = models.CharField(max_length=50, blank=True, verbose_name="NIC")
    mac_address = models.CharField(max_length=50,
                                   blank=True,
                                   verbose_name="MAC Address")
    ip_status = models.ForeignKey(IpStatus,
                                  models.SET_NULL,
                                  null=True,
                                  blank=True,
                                  verbose_name="IP Status")

    def __str__(self):
        return "{}: {}".format(self.ip, self.ip_status)

    class Meta:
        ordering = ['ip']
        verbose_name_plural = "Devices in Net"
