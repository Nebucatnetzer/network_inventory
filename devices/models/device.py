from django.db import models
from core.models import Category, Company
from customers.models import Customer, Owner, Location
from users.models import User
from nets.models import Net, IpStatus


class DeviceManufacturer(Company):

    class Meta:
        verbose_name_plural = "Device Manufacturers"


class DeviceCategory(Category):

    class Meta:
        verbose_name_plural = "Device Categories"


class HardwareModel(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(DeviceManufacturer,
                                     on_delete=models.CASCADE)

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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('device', args=[str(self.id)])


class ConnectedDevice(Device):
    net = models.ManyToManyField(Net, through='DeviceInNet')

    @property
    def nets(self):
        nets_result = DeviceInNet.objects.filter(
            device=self.id).order_by('net')
        nets = []
        for net in nets_result:
            ip_addresses = {}
            ip_addresses['net_id'] = net.net.id
            ip_addresses['ip'] = net.ip
            ip_addresses['name'] = net.net.name
            nets.append(ip_addresses)
        return nets

    class Meta:
        verbose_name_plural = "Connected Devices"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('connected_device', args=[str(self.id)])


class DeviceInNet(models.Model):
    device = models.ForeignKey(ConnectedDevice, on_delete=models.CASCADE)
    net = models.ForeignKey(Net, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField(verbose_name="IP")
    nic = models.CharField(max_length=50, blank=True, verbose_name="NIC")
    mac_address = models.CharField(max_length=50, blank=True,
                                   verbose_name="MAC Address")
    ip_status = models.ForeignKey(IpStatus, models.SET_NULL, null=True,
                                  blank=True, verbose_name="IP Status")

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name_plural = "Devices in Net"
