import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_unauthorized_request_owner(api_client):
    url = reverse('owner-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_owner(api_client_authenticated):
    url = reverse('owner-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_customer(api_client):
    url = reverse('customer-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_customer(api_client_authenticated):
    url = reverse('customer-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_device_manufacturer(api_client):
    url = reverse('devicemanufacturer-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_device_manufacturer(api_client_authenticated):
    url = reverse('devicemanufacturer-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_locaton(api_client):
    url = reverse('location-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_locaton(api_client_authenticated):
    url = reverse('location-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200
