from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.generic import DeleteView

from django_tables2 import RequestConfig

from core import utils
from customers.decorators import customer_view_permission
from customers.models import Customer
from computers.models import Computer
from licenses.models import LicenseWithUser

from .decorators import user_view_permission
from .models import Group
from .models import MailAlias
from .models import User
from .tables import GroupsTable
from .tables import UsersTable


@login_required
@customer_view_permission
def users_table_view(request, pk):
    table = UsersTable(User.objects.filter(customer=pk))
    RequestConfig(request).configure(table)
    return render(request, "users/user_list.html", {"users": table})


@login_required
@user_view_permission
def user_detail_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    groups = Group.objects.filter(user=user)
    mail_alias = MailAlias.objects.filter(user=user)
    computers = Computer.objects.filter(user=user)
    licenses = LicenseWithUser.objects.filter(user=user)
    return render(
        request,
        "users/user_details.html",
        {
            "user": user,
            "groups": groups,
            "mail_alias": mail_alias,
            "computers": computers,
            "licenses": licenses,
        },
    )


class UserDeleteView(LoginRequiredMixin, DeleteView):  # type: ignore
    model = User

    def get_success_url(self):
        return reverse("users", args=(self.object.customer.pk,))


@login_required
@customer_view_permission
def groups_table_view(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    groups_table = GroupsTable(
        utils.get_objects_for_customer(Group, user=request.user, customer_pk=pk)
    )
    RequestConfig(request).configure(groups_table)
    return TemplateResponse(
        request,
        "groups/group_list.html",
        {
            "customer": customer.name,
            "groups": groups_table,
        },
    )


@login_required
def group_detail_view(request, pk):
    group = utils.get_object_with_view_permission(Group, user=request.user, pk=pk)
    users = group.user_set.all()
    groups = Group.objects.filter(parent_group=group)
    print(groups)
    return render(
        request,
        "groups/group_details.html",
        {"group": group, "users": users, "groups": groups},
    )


@login_required
def delete_group(request, pk):
    group = utils.get_object_with_view_permission(Group, user=request.user, pk=pk)
    if request.method == "POST":
        group.delete()
        return redirect("groups", pk=group.customer.pk)
    return TemplateResponse(
        request, "groups/group_confirm_delete.html", {"object": group}
    )
