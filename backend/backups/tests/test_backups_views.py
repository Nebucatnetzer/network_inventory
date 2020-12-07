import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_unauthorized_request_backup_method(api_client):
    url = reverse('backupmethod-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_backup_method(api_client_authenticated):
    url = reverse('backupmethod-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_backup(api_client):
    url = reverse('backup-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_backup(api_client_authenticated):
    url = reverse('backup-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_target_device(api_client):
    url = reverse('targetdevice-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_target_device(api_client_authenticated):
    url = reverse('targetdevice-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_notificaton_from_backup(api_client):
    url = reverse('notificationfrombackup-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_notificaton_from_backup(api_client_authenticated):
    url = reverse('notificationfrombackup-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_notificaton(api_client):
    url = reverse('notification-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_notificaton(api_client_authenticated):
    url = reverse('notification-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized_request_notificaton_type(api_client):
    url = reverse('notificationtype-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authorized_request_notificaton_type(api_client_authenticated):
    url = reverse('notificationtype-list')
    response = api_client_authenticated.get(url)
    assert response.status_code == 200
