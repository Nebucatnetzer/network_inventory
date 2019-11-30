import pytest
from mixer.backend.django import mixer

from django.test import Client

from helper import in_content, not_in_content

pytestmark = pytest.mark.django_db


def test_customer_device_table_not_logged_in():
    response = Client().get('/customer/1/devices/')
    assert response.status_code == 302 and 'login' in response.url
