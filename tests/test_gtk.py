import attr
from dapodik.base import BaseDapodik
from dapodik.gtk import BaseGtk
from dapodik.gtk import Ptk
from dapodik.gtk import PtkTerdaftar
from dapodik.gtk.enums import PtkAktif
from dapodik.gtk.enums import PtkInduk


def test_base_gtk():
    assert issubclass(BaseGtk, BaseDapodik)


def test_member():
    assert attr.has(Ptk)
    assert attr.has(PtkTerdaftar)


def test_enums():
    assert PtkAktif("1") is PtkAktif.AKTIF
    assert bool(PtkAktif("1")) is True
    assert PtkAktif("0") is PtkAktif.NON_AKTIF
    assert bool(PtkAktif("0")) is False
    assert PtkInduk("1") is PtkInduk.INDUK
    assert bool(PtkInduk("1")) is True
    assert PtkInduk("0") is PtkInduk.NON_INDUK
    assert bool(PtkInduk("0")) is False
