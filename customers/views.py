from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView

from django_tables2 import RequestConfig
from guardian.mixins import PermissionRequiredMixin
from guardian.shortcuts import get_objects_for_user

from .models import Customer
from .tables import CustomersTable


@login_required
def customers_table_view(request):
    table = CustomersTable(
        get_objects_for_user(request.user,
                             'customers.view_customer',
                             klass=Customer))
    RequestConfig(request).configure(table)
    return render(request, 'customers/customer_list.html', {'customers': table})


class CustomerDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Customer
    template_name = 'customers/customer_details.html'
    permission_required = 'view_customer'
