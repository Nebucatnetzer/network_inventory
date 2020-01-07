import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


def test_computer_reverse_url():
    computer = mixer.blend('inventory.Computer')
    assert (computer.get_absolute_url()
            == "/computer/" + str(computer.id) + "/")
