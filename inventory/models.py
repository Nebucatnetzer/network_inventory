from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Weekday(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Month(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RamType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Ram(models.Model):
    type = models.ForeignKey(RamType, on_delete=models.CASCADE)
    size_in_gb = models.FloatField()

    def __str__(self):
        return '{} {} GB'.format(self.type, self.size)


class DiskType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class DiskSize(models.Model):
    size = models.FloatField()

    def __str__(self):
        return self.size + " GB"


class Disk(models.Model):
    type = models.ForeignKey(DiskType, on_delete=models.CASCADE)
    size_in_gb = models.ForeignKey(DiskSize, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} GB'.format(self.type, self.size)


class Architecture(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CpuManufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Cpu(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(CpuManufacturer, on_delete=models.PROTECT)
    number_of_cores = models.IntegerField()
    frequency = models.FloatField()
    architecture = models.ForeignKey(Architecture, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class OperatingSystem(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Raid(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Computer(Device):
    hostname = models.CharField(max_length=20, unique=True)
    raid = models.ForeignKey(Raid, null=True, blank=True,
                             on_delete=models.PROTECT)
    os = models.ForeignKey(OperatingSystem, on_delete=models.PROTECT)
    cpu = models.ForeignKey(Cpu, on_delete=models.PROTECT)
    ram = models.ManyToManyField(Ram, through='ComputerRamRelation')
    ip = models.CharField(max_length=15)
    disks = models.ManyToManyField(Disk, through='ComputerDiskRelation')
    host = models.ForeignKey('self', null=True, blank=True,
                             on_delete=models.PROTECT)

    def __str__(self):
        return self.hostname


class ComputerDiskRelation(models.Model):
    disk = models.ForeignKey(Disk, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    amount = models.IntegerField()


class ComputerRamRelation(models.Model):
    ram = models.ForeignKey(Ram, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    amount = models.IntegerField()

class Warranty(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    files = models.FileField()
    valid_until = models.DateField()

    def __str__(self):
        return self.device


class CronJob(models.Model):
    name = models.CharField(max_length=50)
    host = models.ForeignKey(Computer, on_delete=models.CASCADE)
    command = models.CharField(max_length=50)
    time = models.TimeField()
    weekday = models.ForeignKey(Weekday, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
