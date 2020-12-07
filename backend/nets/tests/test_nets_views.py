import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_unauthorized_request_ip_status(api_client):
    url = reverse('ipstatus-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_ip_status(api_client_authenticated):
    url = reverse('ipstatus-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_net(api_client):
    url = reverse('net-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_net(api_client_authenticated):
    url = reverse('net-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200
