from django_tables2 import RequestConfig
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.generic import DeleteView

from core import utils
from .forms import CustomerForm
from .models import Customer
from .tables import CustomersTable


@login_required
def customers_table_view(request):
    customers = utils.get_objects_with_view_permission(Customer, request.user)
    table = CustomersTable(customers)
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
    customer = utils.get_object_with_view_permission(
        Customer, user=request.user, pk=pk)
    context = {'customer': customer}
    return TemplateResponse(request,
                            "customers/customer_details.html",
                            context)


@login_required
def customer_create_view(request):
    """
    A view to create a customer.
    """
    template_name = 'customers/customer_create.html'

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect(customer)
    else:
        form = CustomerForm()
    return TemplateResponse(request, template_name, {'form': form})


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer

    def get_success_url(self):
        return reverse('customers')
