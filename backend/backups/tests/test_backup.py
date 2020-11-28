import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


def test_backup_reverse_url():
    backup = mixer.blend('backups.Backup')
    assert (backup.get_absolute_url()
            == "/backup/" + str(backup.id) + "/")
