import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


def test_device_reverse_url():
    device = mixer.blend('devices.Device')
    assert (device.get_absolute_url()
            == "/device/" + str(device.id) + "/")
