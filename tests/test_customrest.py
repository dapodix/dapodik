import attr

from dapodik.base import BaseDapodik
from dapodik.customrest import BaseCustomrest
from dapodik.customrest import Wilayah


def test_base_customresr():
    assert issubclass(BaseCustomrest, BaseDapodik)


def test_member():
    assert attr.has(Wilayah)
