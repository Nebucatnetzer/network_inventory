from django.conf.urls import url

from inventory import views

urlpatterns = [
    url(r'^$', views.ComputerList.as_view(), name='computers'),
    url(r'^device/(?P<device_id>[0-9]+)/$',
        views.device_details,
        name='device'),
    url(r'^computer/(?P<computer_id>[0-9]+)/$',
        views.computer_details,
        name='computer'),
    url(r'^cronjob/(?P<cronjob_id>[0-9]+)/$',
        views.cronjob_details,
        name='cronjob'),
    url(r'^cronjobs/$', views.CronJobList.as_view(), name='cronjobs'),
    url(r'^devices/$', views.DeviceList.as_view(), name='devices'),
 ]
