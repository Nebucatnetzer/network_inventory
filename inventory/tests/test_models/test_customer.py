import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


def test_customer_reverse_url():
    customer = mixer.blend('customer.Customer')
    assert (customer.get_absolute_url()
            == "/customer/" + str(customer.id) + "/")
