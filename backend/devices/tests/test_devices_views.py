import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_unauthorized_request_warranty(api_client):
    url = reverse('warranty-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_warranty_type(api_client):
    url = reverse('warranty-type-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_device(api_client):
    url = reverse('device-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_device_category(api_client):
    url = reverse('device-category-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_device_in_net(api_client):
    url = reverse('device-in-net-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_device_manufacturer(api_client):
    url = reverse('device-manufacturer-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_hardware_model(api_client):
    url = reverse('hardware-model-list')
    response = api_client.get(url)
    assert response.status_code == 403
