from django.conf.urls import url

from inventory import views

urlpatterns = [
    url(r'^$', views.CustomerList.as_view(), name='customers'),
    url(r'^customer/(?P<customer_id>[0-9]+)/$',
        views.ComputerList.as_view(),
        name='computers'),
    url(r'^device/(?P<device_id>[0-9]+)/$',
        views.device_details,
        name='device'),
    url(r'^computer/(?P<computer_id>[0-9]+)/$',
        views.computer_details,
        name='computer'),
    url(r'^devices/$', views.DeviceList.as_view(), name='devices'),
 ]
