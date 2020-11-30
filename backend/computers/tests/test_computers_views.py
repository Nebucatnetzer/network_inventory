import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_unauthorized_request_computer(api_client):
    url = reverse('computer-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_computer_cpu_relation(api_client):
    url = reverse('computer-cpu-relation-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_computer_disk_relation(api_client):
    url = reverse('computer-disk-relation-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_computer_gpu_relation(api_client):
    url = reverse('computer-gpu-relation-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_computer_ram_relation(api_client):
    url = reverse('computer-ram-relation-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_computer_software_relation(api_client):
    url = reverse('computer-software-relation-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_cpu_architecture(api_client):
    url = reverse('cpu-architecture-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_cpu_manufacturer(api_client):
    url = reverse('cpu-manufacturer-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_cpu(api_client):
    url = reverse('cpu-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_disk_type(api_client):
    url = reverse('disk-type-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_disk(api_client):
    url = reverse('disk-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_gpu_manufacturer(api_client):
    url = reverse('gpu-manufacturer-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_gpu(api_client):
    url = reverse('gpu-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_disks_in_raid(api_client):
    url = reverse('disk-in-raid-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_raid_type(api_client):
    url = reverse('raid-type-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_raid(api_client):
    url = reverse('raid-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_ram_type(api_client):
    url = reverse('ram-type-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_ram(api_client):
    url = reverse('ram-list')
    response = api_client.get(url)
    assert response.status_code == 403
