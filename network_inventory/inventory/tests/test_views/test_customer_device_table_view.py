import pytest

from django.test import Client

pytestmark = pytest.mark.django_db


def test_customer_device_table_not_logged_in():
    response = Client().get('/customer/1/devices/')
    assert response.status_code == 302 and 'login' in response.url
