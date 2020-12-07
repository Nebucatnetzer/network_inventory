import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_unauthorized_request_warranty(api_client):
    url = reverse('warranty-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_warranty_type(api_client_authenticated):
    url = reverse('warrantytype-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_device(api_client):
    url = reverse('device-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_device(api_client_authenticated):
    url = reverse('device-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_device_category(api_client):
    url = reverse('devicecategory-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_device_category(api_client_authenticated):
    url = reverse('devicecategory-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_device_in_net(api_client):
    url = reverse('deviceinnet-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_device_in_net(api_client_authenticated):
    url = reverse('deviceinnet-list')
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
def test_unauthorized_request_hardware_model(api_client):
    url = reverse('hardwaremodel-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_hardware_model(api_client_authenticated):
    url = reverse('hardwaremodel-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200
