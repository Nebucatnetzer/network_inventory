import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_unauthorized_request_user_license(api_client):
    url = reverse('user-license-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_computer_license(api_client):
    url = reverse('computer-license-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_license_with_user(api_client):
    url = reverse('license-with-user-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_license_with_computer(api_client):
    url = reverse('license-with-computer-list')
    response = api_client.get(url)
    assert response.status_code == 403
