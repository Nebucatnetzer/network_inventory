import pytest

from django.test import Client
from mixer.backend.django import mixer

from core.tests import helper
from customers.models import Customer

pytestmark = pytest.mark.django_db


def test_customer_user_table_not_logged_in():
    response = Client().get("/customer/1/users/")
    assert response.status_code == 302 and "login" in response.url


def test_customer_user_table(create_admin_user):
    fixture = create_admin_user()
    customer = fixture["customer"]
    client = Client()
    client.login(username="pharma-admin", password="password")
    user = mixer.blend("users.User", customer=mixer.SELECT)
    group = mixer.blend("users.Group")
    mixer.blend("users.UserInGroup", user=user, group=group)
    response = client.get("/customer/" + str(customer.id) + "/users/")
    assert (
        response.status_code == 200
        and helper.in_content(response, user.name)
        and helper.in_content(response, group)
        and helper.in_content(response, user.primary_mail)
    )


def test_customer_user_table_no_user(create_admin_user):
    fixture = create_admin_user()
    customer = fixture["customer"]
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get("/customer/" + str(customer.id) + "/users/")
    assert response.status_code == 200 and helper.not_in_content(response, customer)


def test_customer_user_table_no_permission(create_admin_user):
    create_admin_user()
    customer = Customer.objects.create(name="Water Corp.")
    client = Client()
    client.login(username="pharma-admin", password="password")
    mixer.blend("users.User", customer=customer)
    response = client.get("/customer/" + str(customer.id) + "/users/")
    assert response.status_code == 403


def test_customer_user_table_multiple_users(create_admin_user):
    fixture = create_admin_user()
    customer = fixture["customer"]
    client = Client()
    client.login(username="pharma-admin", password="password")
    user1 = mixer.blend("users.User", customer=mixer.SELECT)
    user2 = mixer.blend("users.User", customer=mixer.SELECT)
    response = client.get("/customer/" + str(customer.id) + "/users/")
    assert (
        response.status_code == 200
        and helper.in_content(response, user1.name)
        and helper.in_content(response, user2.name)
    )
