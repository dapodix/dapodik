import attr
from dapodik.base import BaseDapodik
from dapodik.rombongan_belajar import AnggotaRombel
from dapodik.rombongan_belajar import Pembelajaran
from dapodik.rombongan_belajar import RombelPortal
from dapodik.rombongan_belajar import RombonganBelajar
from dapodik.rombongan_belajar import BaseRombonganBelajar


def test_base_rombongan_belajar():
    assert issubclass(BaseRombonganBelajar, BaseDapodik)


def test_member():
    assert attr.has(AnggotaRombel)
    assert attr.has(Pembelajaran)
    assert attr.has(RombelPortal)
    assert attr.has(RombonganBelajar)
