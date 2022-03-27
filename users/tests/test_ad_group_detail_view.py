import pytest
from mixer.backend.django import mixer

from django.test import Client

from core.tests import helper

pytestmark = pytest.mark.django_db


def test_ad_group_detail_view_not_logged_in():
    response = Client().get("/ad-group/1/")
    assert response.status_code == 302 and "login" in response.url


def test_ad_group_detail_view(create_admin_user):
    create_admin_user()
    group = mixer.blend("users.AdGroup", customer=mixer.SELECT)
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get("/ad-group/" + str(group.id) + "/")
    assert response.status_code == 200 and helper.in_content(response, group)


def test_ad_group_detail_view_not_found(create_admin_user):
    create_admin_user()
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get("/ad-group/230/")
    assert response.status_code == 404


def test_ad_group_detail_view_no_permission(create_admin_user):
    create_admin_user()
    customer = mixer.blend("customers.Customer")
    group = mixer.blend("users.AdGroup", customer=customer)
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get("/ad-group/" + str(group.id) + "/")
    assert response.status_code == 404


def test_ad_group_detail_view_with_user(create_admin_user):
    create_admin_user()
    group = mixer.blend("users.AdGroup", customer=mixer.SELECT)
    client = Client()
    client.login(username="pharma-admin", password="password")
    response = client.get("/ad-group/" + str(group.id) + "/")
    user = mixer.blend("users.User", customer=mixer.SELECT)
    user.ad_groups.add(group)
    response = client.get("/ad-group/" + str(group.id) + "/")
    assert response.status_code == 200 and helper.in_content(response, user)
