import pytest

from core.models import DayOfMonth
from core.templatetags import core_extras


def test_verbose_name():
    instance = DayOfMonth()
    assert "day of month" == core_extras.verbose_name(instance)
