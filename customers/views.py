from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import DetailView

from django_tables2 import RequestConfig
from guardian.mixins import PermissionRequiredMixin

from core import utils
from .models import Customer
from .tables import CustomersTable


@login_required
def customers_table_view(request):
    table = CustomersTable(utils.get_customers(request.user))
    RequestConfig(request).configure(table)
    return render(request,
                  'customers/customer_list.html',
                  {'customers': table})


class CustomerDetailView(LoginRequiredMixin,
                         PermissionRequiredMixin,
                         DetailView):
    model = Customer
    template_name = 'customers/customer_details.html'
    permission_required = 'view_customer'


class CustomerCreateView(LoginRequiredMixin, CreateView):
    """
    A view to create a customer.
    """
    model = Customer
    template_name = 'customers/customer_create.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('customer', args=(self.object.pk,))
