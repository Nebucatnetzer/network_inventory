import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_unauthorized_request_weekday(api_client):
    url = reverse('weekday-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_weekday(api_client_authenticated):
    url = reverse('weekday-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_month(api_client):
    url = reverse('month-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_month(api_client_authenticated):
    url = reverse('month-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_day_of_month(api_client):
    url = reverse('dayofmonth-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_day_of_month(api_client_authenticated):
    url = reverse('dayofmonth-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_hours_in_day(api_client):
    url = reverse('hoursinday-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_hours_in_day(api_client_authenticated):
    url = reverse('hoursinday-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_minutes_in_hour(api_client):
    url = reverse('minutesinhour-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_minutes_in_hour(api_client_authenticated):
    url = reverse('minutesinhour-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200
