import attr
from dapodik.base import BaseDapodik
from dapodik.peserta_didik import BasePesertaDidik
from dapodik.peserta_didik import CreatePesertaDidik
from dapodik.peserta_didik import PesertaDidikBaru
from dapodik.peserta_didik import PesertaDidikLongitudinal
from dapodik.peserta_didik import RegistrasiPesertaDidik
from dapodik.peserta_didik import PesertaDidik


def test_base_peserta_didik():
    assert issubclass(BasePesertaDidik, BaseDapodik)


def test_member():
    assert attr.has(CreatePesertaDidik)
    assert attr.has(PesertaDidikBaru)
    assert attr.has(PesertaDidikLongitudinal)
    assert attr.has(RegistrasiPesertaDidik)
    assert attr.has(PesertaDidik)
