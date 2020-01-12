from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django_tables2 import RequestConfig

from computers.models import Computer
from customers.decorators import customer_view_permission

from .decorators import backup_view_permission
from .models import Backup
from .models import NotificationFromBackup
from .models import TargetDevice
from .tables import BackupsTable


@login_required
@customer_view_permission
def backups_table_view(request, pk):
    computers = Computer.objects.filter(customer=pk)
    table = BackupsTable(Backup.objects.filter(computer__in=computers))
    RequestConfig(request).configure(table)
    return render(request, 'backups/backup_list.html', {'backups': table})


@login_required
@backup_view_permission
def backup_detail_view(request, pk):
    backup = get_object_or_404(Backup, pk=pk)
    target_device_list = TargetDevice.objects.filter(backup=backup)
    notifications = NotificationFromBackup.objects.filter(backup=backup)
    return render(request, 'backups/backup_details.html',
                  {'backup': backup,
                   'target_device_list': target_device_list,
                   'notifications': notifications})
