from datetime import datetime
from datetime import timedelta
import pytest
from mixer.backend.django import mixer

from django.test import Client

from core.tests import helper

pytestmark = pytest.mark.django_db


def test_warranties_view_not_logged_in():
    response = Client().get("/warranties/")
    assert response.status_code == 302 and "login" in response.url


def test_warranties_no_warranties_found(create_admin_user):
    create_admin_user()
    client = Client()
    customer = mixer.blend("customers.Customer")
    device = mixer.blend("devices.Device", customer=customer)
    warranty = mixer.blend(
        "devices.Warranty",
        device=device,
        valid_from="1999-01-01",
        valid_until="2000-01-01",
    )
    client.login(username="pharma-admin", password="password")
    response = client.get("/warranties/")
    assert response.status_code == 200 and helper.not_in_content(
        response, warranty.customer
    )


def test_warranties_view_plenty_of_time(create_admin_user):
    fixture = create_admin_user()
    user = fixture["admin"]
    user.save()
    device = mixer.blend("devices.Device", customer=fixture["customer"])
    more_than_one_year = datetime.date(datetime.today() + timedelta(400))
    mixer.blend("devices.Warranty", device=device, valid_until=more_than_one_year)
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get("/warranties/")
    # Problems with the bgcolor attribute prevent the use of helper.in_content
    assert (
        response.status_code == 200
        and ('bgcolor="orange"' not in response.content.decode("utf8"))
        and ('bgcolor="red"' not in response.content.decode("utf8"))
    )


def test_warranties_view_warranty_expired(create_admin_user):
    fixture = create_admin_user()
    device = mixer.blend("devices.Device", customer=fixture["customer"])
    mixer.blend(
        "devices.Warranty",
        device=device,
        valid_from="1999-01-01",
        valid_until="2000-01-01",
    )
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get("/warranties/")
    # Problems with the bgcolor attribute prevent the use of helper.in_content
    assert response.status_code == 200 and (
        'bgcolor="red"' in response.content.decode("utf8")
    )


def test_warranties_view_warranty_one_year_till_expiration(create_admin_user):
    fixture = create_admin_user()
    user = fixture["admin"]
    user.save()
    device = mixer.blend("devices.Device", customer=fixture["customer"])
    not_one_year_more = datetime.date(datetime.today() + timedelta(200))
    mixer.blend("devices.Warranty", device=device, valid_until=not_one_year_more)
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get("/warranties/")
    # Problems with the bgcolor attribute prevent the use of helper.in_content
    assert response.status_code == 200 and (
        'bgcolor="orange"' in response.content.decode("utf8")
    )
