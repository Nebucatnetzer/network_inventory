import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_unauthorized_request_backup_method(api_client):
    url = reverse('backup-method-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_backup(api_client):
    url = reverse('backup-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_target_device(api_client):
    url = reverse('target-device-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_notificaton_from_backup(api_client):
    url = reverse('notification-from-backup-list')
    response = api_client.get(url)
    assert response.status_code == 403
