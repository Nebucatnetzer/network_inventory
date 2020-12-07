import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_unauthorized_request_operating_system(api_client):
    url = reverse('operatingsystem-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_operating_system(api_client_authenticated):
    url = reverse('operatingsystem-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_software_architecture(api_client):
    url = reverse('softwarearchitecture-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_software_architecture(api_client_authenticated):
    url = reverse('softwarearchitecture-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_software_category(api_client):
    url = reverse('softwarecategory-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_software_category(api_client_authenticated):
    url = reverse('softwarecategory-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_software(api_client):
    url = reverse('software-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_software(api_client_authenticated):
    url = reverse('software-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200
