from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from django_tables2 import RequestConfig

from customers.decorators import customer_view_permission
from computers.models import Computer
from licenses.models import LicenseWithUser

from .decorators import user_view_permission
from .models import MailAlias
from .models import User
from .models import UserInAdGroup
from .models import UserInMailGroup
from .tables import UsersTable


@login_required
@customer_view_permission
def users_table_view(request, pk):
    table = UsersTable(User.objects.filter(customer=pk))
    RequestConfig(request).configure(table)
    return render(request, 'users/user_list.html', {'users': table})


@login_required
@user_view_permission
def user_detail_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    ad_groups = UserInAdGroup.objects.filter(user=user)
    mail_groups = UserInMailGroup.objects.filter(user=user)
    mail_alias = MailAlias.objects.filter(user=user)
    computers = Computer.objects.filter(user=user)
    licenses = LicenseWithUser.objects.filter(user=user)
    return render(request, 'users/user_details.html',
                  {'user': user,
                   'ad_groups': ad_groups,
                   'mail_groups': mail_groups,
                   'mail_alias': mail_alias,
                   'computers': computers,
                   'licenses': licenses})
