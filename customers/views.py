from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import Http404
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django_tables2 import RequestConfig

from core import utils
from .forms import CustomerForm
from .models import Customer
from .tables import CustomersTable


@login_required
def customers_table_view(request):
    table = CustomersTable(utils.get_customers(request.user))
    RequestConfig(request).configure(table)
    return render(request,
                  'customers/customer_list.html',
                  {'customers': table})


@login_required
def htmx_create_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("<script>location.reload()</script>")
        else:
            return TemplateResponse(request,
                                    "customers/partials/customer_create.html",
                                    context={"form": form})
    form = CustomerForm()
    context = {"form": form}
    return TemplateResponse(request,
                            "customers/partials/customer_create.html",
                            context)


@login_required
def customer_detail_view(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    permission = request.user.has_perm('customers.view_customer',
                                       customer)
    if permission:
        context = {'customer': customer}
        return TemplateResponse(request,
                                "customers/customer_details.html",
                                context)
    else:
        raise Http404()


class CustomerCreateView(LoginRequiredMixin, CreateView):
    """
    A view to create a customer.
    """
    model = Customer
    template_name = 'customers/customer_create.html'
    fields = ['name', 'description']

    def get_success_url(self):
        return reverse('customer', args=(self.object.pk,))


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer

    def get_success_url(self):
        return reverse('customers')
