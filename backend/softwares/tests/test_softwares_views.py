import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_unauthorized_request_operating_system(api_client):
    url = reverse('operating-system-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_software_architecture(api_client):
    url = reverse('software-architecture-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_software_category(api_client):
    url = reverse('software-category-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_software(api_client):
    url = reverse('software-list')
    response = api_client.get(url)
    assert response.status_code == 403
