import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_unauthorized_request_computer(api_client):
    url = reverse('computer-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_computer_cpu_relation(api_client):
    url = reverse('computercpurelation-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_computer_disk_relation(api_client):
    url = reverse('computerdiskrelation-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_computer_gpu_relation(api_client):
    url = reverse('computergpurelation-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_computer_ram_relation(api_client):
    url = reverse('computerramrelation-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_computer_software_relation(api_client):
    url = reverse('computersoftwarerelation-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_cpu_architecture(api_client):
    url = reverse('cpuarchitecture-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_cpu_manufacturer(api_client):
    url = reverse('cpumanufacturer-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_cpu(api_client):
    url = reverse('cpu-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_disk_type(api_client):
    url = reverse('disktype-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_disk(api_client):
    url = reverse('disk-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_gpu_manufacturer(api_client):
    url = reverse('gpumanufacturer-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_gpu(api_client):
    url = reverse('gpu-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_disks_in_raid(api_client):
    url = reverse('disksinraid-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_raid_type(api_client):
    url = reverse('raidtype-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_raid(api_client):
    url = reverse('raid-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_ram_type(api_client):
    url = reverse('ramtype-list')
    response = api_client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthorized_request_ram(api_client):
    url = reverse('ram-list')
    response = api_client.get(url)
    assert response.status_code == 403
