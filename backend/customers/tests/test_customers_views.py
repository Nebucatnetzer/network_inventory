import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_unauthorized_request_onwer(api_client):
    url = reverse('owner-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_customer(api_client):
    url = reverse('customer-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_device_manufacturer(api_client):
    url = reverse('device-manufacturer-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_locaton(api_client):
    url = reverse('location-list')
    response = api_client.get(url)
    assert response.status_code == 403
