from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Weekday(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()

    def __str__(self):
        return self.name


class DayOfMonth(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Days of Month"


class Month(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()

    def __str__(self):
        return self.name


class RamType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Types of RAM Modules"


class Ram(models.Model):
    type = models.ForeignKey(RamType, on_delete=models.CASCADE)
    size_in_gb = models.IntegerField()
    ecc = models.BooleanField(default=False)

    def __str__(self):
        return '{} {} GB'.format(self.type, self.size_in_gb)

    class Meta:
        verbose_name_plural = "RAM Modules"


class DiskType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Types of disks"


class DiskSize(models.Model):
    size = models.IntegerField()

    def __str__(self):
        return str(self.size) + " GB"

    class Meta:
        verbose_name_plural = "Disk sizes"


class Disk(models.Model):
    type = models.ForeignKey(DiskType, on_delete=models.CASCADE)
    size_in_gb = models.ForeignKey(DiskSize, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.type, self.size_in_gb)


class Architecture(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CpuManufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "CPU Manufacturers"


class Cpu(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(CpuManufacturer, on_delete=models.PROTECT)
    number_of_cores = models.IntegerField()
    frequency = models.FloatField()
    architecture = models.ForeignKey(Architecture, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "CPUs"


class OperatingSystem(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Operating Systems"


class Raid(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Types of RAID"


class Computer(Device):
    hostname = models.CharField(max_length=20, unique=True)
    os = models.ForeignKey(OperatingSystem, on_delete=models.PROTECT)
    cpu = models.ManyToManyField(Cpu, through='ComputerCpuRelation')
    ram = models.ManyToManyField(Ram, through='ComputerRamRelation')
    ip = models.CharField(max_length=15)
    disks = models.ManyToManyField(Disk, through='ComputerDiskRelation')
    host = models.ForeignKey('self', null=True, blank=True,
                             on_delete=models.PROTECT)

    def __str__(self):
        return str(self.hostname)


class ComputerDiskRelation(models.Model):
    disk = models.ForeignKey(Disk, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    amount = models.IntegerField()
    raid = models.ForeignKey(Raid, null=True, blank=True,
                             on_delete=models.PROTECT)

    def __str__(self):
        return self.computer.hostname

    class Meta:
        verbose_name_plural = "Disks in Computer"


class ComputerRamRelation(models.Model):
    ram = models.ForeignKey(Ram, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return self.computer.hostname

    class Meta:
        verbose_name_plural = "RAM Modules in Computer"


class ComputerCpuRelation(models.Model):
    cpu = models.ForeignKey(Cpu, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return self.computer.hostname

    class Meta:
        verbose_name_plural = "CPUs in Computer"


class Warranty(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    files = models.FileField()
    valid_until = models.DateField()

    def __str__(self):
        return self.device

    class Meta:
        verbose_name_plural = "Warranties"


class CronJob(models.Model):
    name = models.CharField(max_length=50)
    host = models.ForeignKey(Computer, on_delete=models.CASCADE)
    command = models.CharField(max_length=50)
    time = models.TimeField()
    weekday = models.ForeignKey(Weekday, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cron Jobs"
