import attr
from dapodik.auth import BaseAuth
from dapodik.auth import Pengguna
from dapodik.base import BaseDapodik


def test_base_auth():
    assert issubclass(BaseAuth, BaseDapodik)


def test_member():
    assert attr.has(Pengguna)
