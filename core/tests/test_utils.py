from django.http import Http404
import pytest

from core import utils

pytestmark = pytest.mark.django_db


def test_get_objects_raises_404(create_admin_user):
    fixture = create_admin_user()
    with pytest.raises(Http404):
        utils.get_objects("WrongModelName", fixture['admin'])
