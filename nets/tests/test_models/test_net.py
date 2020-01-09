import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


def test_net_reverse_url():
    net = mixer.blend('nets.Net')
    assert (net.get_absolute_url()
            == "/net/" + str(net.id) + "/")
