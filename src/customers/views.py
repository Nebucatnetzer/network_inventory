from django_tables2 import RequestConfig
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.generic import DeleteView

from crispy_forms.utils import render_crispy_form
from crispy_forms.templatetags.crispy_forms_filters import as_crispy_field

from core import utils
from .forms import CustomerForm
from .forms import DummyLocationForm
from .forms import LocationForm
from .models import Customer, DummyLocation
from .tables import CustomersTable


@login_required
def customers_table_view(request):
    customers = utils.objects_for_allowed_customers(Customer, request.user)
    table = CustomersTable(customers)
    RequestConfig(request).configure(table)
    return render(request, "customers/customer_list.html", {"customers": table})


@login_required
def create_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("<script>location.reload()</script>")
        else:
            return TemplateResponse(
                request,
                "customers/partials/customer_create.html",
                context={"form": form},
            )
    form = CustomerForm()
    context = {"form": form}
    return TemplateResponse(request, "customers/partials/customer_create.html", context)


@login_required
def customer_detail_view(request, pk):
    customer = utils.get_object_with_view_permission(Customer, user=request.user, pk=pk)
    context = {"customer": customer}
    return TemplateResponse(request, "customers/customer_details.html", context)


class CustomerDeleteView(LoginRequiredMixin, DeleteView):  # type: ignore
    model = Customer

    def get_success_url(self):
        return reverse("customers")


@login_required
def htmx_create_location(request):
    context = {}
    user = request.user
    if request.method == "POST" and "save_location" in request.POST:
        form = LocationForm(request.POST, user=user)
        if form.is_valid():
            location = form.save(commit=True)
            dummy_model = DummyLocation()
            dummy_model.location = location
            dummy_form = DummyLocationForm(instance=dummy_model)
            form_html = as_crispy_field(dummy_form["location"])
        else:
            context.update(csrf(request))
            form.helper.attrs["hx-swap-oob"] = "true"
            form_html = render_crispy_form(form)
        context["valid"] = form.is_valid()
        context["form"] = form_html
        template_path = "customers/partials/location_response.html"
        return TemplateResponse(request, template_path, context)

    form = LocationForm(user=user)
    context["form"] = form
    template_path = "customers/partials/location_create.html"
    return TemplateResponse(request, template_path, context)
