import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_unauthorized_request_user_license(api_client):
    url = reverse('userlicense-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_user_license(api_client_authenticated):
    url = reverse('userlicense-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_computer_license(api_client):
    url = reverse('computerlicense-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_computer_license(api_client_authenticated):
    url = reverse('computerlicense-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_license_with_user(api_client):
    url = reverse('licensewithuser-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_license_with_user(api_client_authenticated):
    url = reverse('licensewithuser-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_license_with_computer(api_client):
    url = reverse('licensewithcomputer-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_license_with_computer(api_client_authenticated):
    url = reverse('licensewithcomputer-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200
