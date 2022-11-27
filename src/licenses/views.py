from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import DeleteView

from django_tables2 import RequestConfig

from customers.decorators import customer_view_permission

from computers.models import Computer

from .models import ComputerLicense
from .models import UserLicense
from .models import LicenseWithComputer
from .tables import ComputerLicensesTable
from .tables import UserLicensesTable


@login_required
@customer_view_permission
def licenses_table_view(request, pk):
    user_licenses = UserLicensesTable(UserLicense.objects.filter(customer=pk))
    computer_licenses = ComputerLicensesTable(
        ComputerLicense.objects.filter(customer=pk)
    )
    RequestConfig(request).configure(user_licenses)
    RequestConfig(request).configure(computer_licenses)
    return render(
        request,
        "licenses/license_list.html",
        {
            "user_licenses": user_licenses,
            "computer_licenses": computer_licenses,
        },
    )


class LicenseWithComputerCreateView(LoginRequiredMixin, CreateView):
    model = LicenseWithComputer
    template_name = "licenses/license_with_computer_create.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse("computer", args=(self.computer.pk,))

    def get_initial(self):
        """
        Set the device and customer dropdown to the device from the previous
        view and the customer related to the device.
        """
        self.computer = get_object_or_404(Computer, id=self.kwargs.get("pk"))
        return {
            "computer": self.computer,
        }


class LicenseWithComputerDeleteView(LoginRequiredMixin, DeleteView):
    model = LicenseWithComputer
    template_name = "licenses/license_with_computer_confirm_delete.html"

    def get_success_url(self):
        return reverse("computer", args=(self.object.computer.pk,))


class UserLicenseDeleteView(LoginRequiredMixin, DeleteView):
    model = UserLicense
    template_name = "licenses/license_confirm_delete.html"

    def get_success_url(self):
        return reverse("licenses", args=(self.object.customer.pk,))


class ComputerLicenseDeleteView(LoginRequiredMixin, DeleteView):
    model = ComputerLicense
    template_name = "licenses/license_confirm_delete.html"

    def get_success_url(self):
        return reverse("licenses", args=(self.object.customer.pk,))
