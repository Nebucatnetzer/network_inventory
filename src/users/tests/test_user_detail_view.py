import pytest
from mixer.backend.django import mixer

from django.test import Client

from core.tests import helper

pytestmark = pytest.mark.django_db


def test_user_detail_view_not_logged_in():
    response = Client().get("/user/1/")
    assert response.status_code == 302 and "login" in response.url


def test_user_detail_view(create_admin_user):
    create_admin_user()
    user = mixer.blend("users.User", customer=mixer.SELECT)
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get("/user/" + str(user.id) + "/")
    assert response.status_code == 200 and helper.in_content(response, user)


def test_user_detail_view_not_found(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get("/user/230/")
    assert response.status_code == 404


def test_user_detail_view_group(create_admin_user):
    create_admin_user()
    user = mixer.blend("users.User", customer=mixer.SELECT)
    login = mixer.blend("users.Login", user=user)
    group = mixer.blend("users.Group")
    mixer.blend("users.LoginInGroup", login=login, group=group)
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get("/user/" + str(user.id) + "/")
    assert response.status_code == 200 and helper.in_content(response, "Groups")


def test_user_detail_view_mail_alias(create_admin_user):
    create_admin_user()
    user = mixer.blend("users.User", customer=mixer.SELECT)
    login = mixer.blend("users.Login", user=user)
    mixer.blend("users.MailAlias", login=login)
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get("/user/" + str(user.id) + "/")
    assert response.status_code == 200 and helper.in_content(response, "Mail Alias")


def test_user_detail_view_license(create_admin_user):
    create_admin_user()
    user = mixer.blend("users.User", customer=mixer.SELECT)
    mixer.blend("licenses.UserLicense", software=mixer.SELECT)
    mixer.blend("licenses.LicenseWithUser", user=user)
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get("/user/" + str(user.id) + "/")
    assert response.status_code == 200 and helper.in_content(response, "License")


def test_user_detail_view_computer(create_admin_user):
    create_admin_user()
    user = mixer.blend("users.User", customer=mixer.SELECT)
    computer = mixer.blend("computers.Computer", user=user)
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get("/user/" + str(user.id) + "/")
    assert response.status_code == 200 and helper.in_content(response, computer)


def test_user_detail_view_no_permission(create_admin_user):
    create_admin_user()
    customer = mixer.blend("customers.Customer")
    user = mixer.blend("users.User", customer=customer)
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get("/user/" + str(user.id) + "/")
    assert response.status_code == 403
