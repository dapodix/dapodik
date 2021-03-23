import attr
from dapodik.base import BaseDapodik
from dapodik.validasi import Validasi
from dapodik.validasi import ValidasiSekolah
from dapodik.validasi import ValidasiPrasarana
from dapodik.validasi import ValidasiPesertaDidik
from dapodik.validasi import ValidasiPtk
from dapodik.validasi import ValidasiRombonganBelajar
from dapodik.validasi import ValidasiPembelajaran
from dapodik.validasi import ValidasiNilai
from dapodik.validasi import ValidasiReferensi
from dapodik.validasi import BaseValidasi


def test_base_validasi():
    assert issubclass(BaseValidasi, BaseDapodik)


def test_member():
    assert attr.has(Validasi)
    assert attr.has(ValidasiSekolah)
    assert issubclass(ValidasiSekolah, Validasi)
    assert attr.has(ValidasiPrasarana)
    assert issubclass(ValidasiPrasarana, Validasi)
    assert attr.has(ValidasiPesertaDidik)
    assert issubclass(ValidasiPesertaDidik, Validasi)
    assert attr.has(ValidasiPtk)
    assert issubclass(ValidasiPtk, Validasi)
    assert attr.has(ValidasiRombonganBelajar)
    assert issubclass(ValidasiRombonganBelajar, Validasi)
    assert attr.has(ValidasiPembelajaran)
    assert issubclass(ValidasiPembelajaran, Validasi)
    assert attr.has(ValidasiNilai)
    assert issubclass(ValidasiNilai, Validasi)
    assert attr.has(ValidasiReferensi)
    assert issubclass(ValidasiReferensi, Validasi)
