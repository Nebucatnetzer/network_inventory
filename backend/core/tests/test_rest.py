import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_unauthorized_request_weekday(api_client):
    url = reverse('weekday-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_month(api_client):
    url = reverse('month-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_day_of_month(api_client):
    url = reverse('dayofmonth-list')
    response = api_client.get(url)
    assert response.status_code == 403
