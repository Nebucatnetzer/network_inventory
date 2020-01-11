from django.shortcuts import render

# Create your views here.


@login_required
@customer_view_permission
def licenses_table_view(request, pk):
    user_licenses = UserLicensesTable(UserLicense.objects.filter(customer=pk))
    computer_licenses = ComputerLicensesTable(
        ComputerLicense.objects.filter(customer=pk))
    RequestConfig(request).configure(user_licenses)
    RequestConfig(request).configure(computer_licenses)
    return render(request,
                  'inventory/license_list.html',
                  {'user_licenses': user_licenses,
                   'computer_licenses': computer_licenses})
