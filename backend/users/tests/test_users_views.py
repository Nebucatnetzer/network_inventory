import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_unauthorized_request_user(api_client):
    url = reverse('computer-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_user(api_client_authenticated):
    url = reverse('computer-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_user_in_ad_group(api_client):
    url = reverse('computer-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_user_in_ad_group(api_client_authenticated):
    url = reverse('computer-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_user_in_mail_group(api_client):
    url = reverse('computer-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_user_in_mail_group(api_client_authenticated):
    url = reverse('computer-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_ad_group(api_client):
    url = reverse('computer-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_ad_group(api_client_authenticated):
    url = reverse('computer-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_mail_group(api_client):
    url = reverse('computer-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_mail_group(api_client_authenticated):
    url = reverse('computer-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_mail_alias(api_client):
    url = reverse('computer-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_mail_alias(api_client_authenticated):
    url = reverse('computer-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200
