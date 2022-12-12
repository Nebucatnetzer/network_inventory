import pytest
from mixer.backend.django import mixer
from django.db import IntegrityError


pytestmark = pytest.mark.django_db


def test_license_two_licenses_per_user():
    mixer.blend("users.User")
    mixer.blend("licenses.UserLicense")
    with pytest.raises(IntegrityError):
        mixer.cycle(2).blend(
            "licenses.LicenseWithUser", user=mixer.SELECT, license=mixer.SELECT
        )


def test_license_two_licenses_per_computer():
    mixer.blend("computers.Computer")
    mixer.blend("licenses.ComputerLicense")
    with pytest.raises(IntegrityError):
        mixer.cycle(2).blend(
            "licenses.LicenseWithComputer",
            computer=mixer.SELECT,
            license=mixer.SELECT,
        )
