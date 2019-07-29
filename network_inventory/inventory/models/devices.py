from django.db import models
from .category import Category
from .companies import Customer, Owner, DeviceManufacturer
from .location import Location
from .user import User
from .net import Net, IpStatus


class DeviceCategory(Category):

    class Meta:
        verbose_name_plural = "Device Categories"


class Device(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    serialnumber = models.CharField(max_length=50, blank=True)
    category = models.ForeignKey(DeviceCategory, on_delete=models.SET_NULL,
                                 null=True, blank=True)
    owner = models.ForeignKey(Owner, models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey(Customer, models.SET_NULL, null=True,
                                 blank=True)
    manufacturer = models.ForeignKey(DeviceManufacturer, models.SET_NULL,
                                     null=True, blank=True)
    location = models.ForeignKey(Location, models.SET_NULL, null=True,
                                 blank=True)
    user = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    installation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class ConnectedDevice(Device):
    net = models.ManyToManyField(Net, through='DeviceInNet')

    @property
    def ips(self):
        nets = DeviceInNet.objects.filter(device=self.id)
        ip_addresses = {}
        for net in nets:
            ip_addresses[net.net_id] = net.ip
        return ip_addresses

    class Meta:
        verbose_name_plural = "Connected Devices"


class DeviceInNet(models.Model):
    device = models.ForeignKey(ConnectedDevice, on_delete=models.CASCADE)
    net = models.ForeignKey(Net, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    nic = models.CharField(max_length=50, blank=True)
    mac_address = models.CharField(max_length=50, blank=True)
    ip_status = models.ForeignKey(IpStatus, models.SET_NULL, null=True,
                                  blank=True)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name_plural = "Devices in Net"
