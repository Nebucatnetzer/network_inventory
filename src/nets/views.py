from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DeleteView
from django_tables2 import RequestConfig

from customers.decorators import customer_view_permission
from devices.models import DeviceInNet

from .decorators import net_view_permission
from .models import Net
from .tables import NetDetailTable
from .tables import NetsTable


@login_required
@customer_view_permission
def nets_table_view(request, pk):
    table = NetsTable(Net.objects.filter(customer=pk))
    RequestConfig(request).configure(table)
    return render(request, "nets/net_list.html", {"nets": table})


@login_required
@net_view_permission
def net_detail_view(request, pk):
    net = get_object_or_404(Net, pk=pk)
    table = NetDetailTable(DeviceInNet.objects.filter(net=net))
    RequestConfig(request).configure(table)
    return render(request, "nets/net_details.html", {"table": table, "net": net})


class NetDeleteView(LoginRequiredMixin, DeleteView):  # type: ignore
    model = Net

    def get_success_url(self):
        return reverse("nets", args=(self.object.customer.pk,))
