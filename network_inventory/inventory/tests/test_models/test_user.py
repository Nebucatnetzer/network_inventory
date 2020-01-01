import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


def test_user_reverse_url():
    user = mixer.blend('inventory.User')
    assert (user.get_absolute_url()
            == "/user/" + str(user.id) + "/")
