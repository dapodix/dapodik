from dapodik import Dapodik
from dapodik.base import BaseDapodik
from dapodik.auth import BaseAuth
from dapodik.peserta_didik import BasePesertaDidik
from dapodik.rest import BaseRest
from dapodik.rombongan_belajar import BaseRombonganBelajar
from dapodik.sarpras import BaseSarpras
from dapodik.sekolah import BaseSekolah
from dapodik.validasi import BaseValidasi


def test_dapodik():
    assert issubclass(Dapodik, BaseDapodik)
    assert issubclass(Dapodik, BaseAuth)
    assert issubclass(Dapodik, BasePesertaDidik)
    assert issubclass(Dapodik, BaseRest)
    assert issubclass(Dapodik, BaseRombonganBelajar)
    assert issubclass(Dapodik, BaseSarpras)
    assert issubclass(Dapodik, BaseSekolah)
    assert issubclass(Dapodik, BaseValidasi)
