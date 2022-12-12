import pytest
from mixer.backend.django import mixer

from django.test import Client

from core.tests import helper
from customers.models import Customer

pytestmark = pytest.mark.django_db


def test_customer_computer_table_not_logged_in():
    response = Client().get("/customer/1/computers/")
    assert response.status_code == 302 and "login" in response.url


def test_customer_computer_table(create_admin_user):
    fixture = create_admin_user()
    customer = fixture["customer"]
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer = mixer.blend("computers.Computer", customer=mixer.SELECT)
    response = client.get("/customer/" + str(customer.id) + "/computers/")
    assert response.status_code == 200 and helper.in_content(
        response, computer
    )


def test_customer_computer_table_no_computer(create_admin_user):
    fixture = create_admin_user()
    customer = fixture["customer"]
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get("/customer/" + str(customer.id) + "/computers/")
    assert response.status_code == 200 and helper.not_in_content(
        response, "Pharma Corp. PC"
    )


def test_customer_computer_table_no_permission(create_admin_user):
    create_admin_user()
    customer = Customer.objects.create(name="Water Corp.")
    client = Client()
    client.login(username="pharma-admin", password="password")
    mixer.blend("computers.Computer", customer=customer)
    response = client.get("/customer/" + str(customer.id) + "/computers/")
    assert response.status_code == 404


def test_customer_computer_table_multiple_computers(create_admin_user):
    fixture = create_admin_user()
    customer = fixture["customer"]
    client = Client()
    client.login(username="pharma-admin", password="password")
    computer1 = mixer.blend("computers.Computer", customer=mixer.SELECT)
    computer2 = mixer.blend("computers.Computer", customer=mixer.SELECT)
    response = client.get("/customer/" + str(customer.id) + "/computers/")
    assert (
        response.status_code == 200
        and helper.in_content(response, computer1)
        and helper.in_content(response, computer2)
    )
