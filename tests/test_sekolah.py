import attr
from dapodik.base import BaseDapodik
from dapodik.sekolah import AkreditasiSp
from dapodik.sekolah import BlockGrant
from dapodik.sekolah import JurusanSp
from dapodik.sekolah import Kepanitiaan
from dapodik.sekolah import ProgramInklusi
from dapodik.sekolah import Sanitasi
from dapodik.sekolah import SekolahLongitudinal
from dapodik.sekolah import SekolahPaud
from dapodik.sekolah import Sekolah
from dapodik.sekolah import Semester
from dapodik.sekolah import Yayasan
from dapodik.sekolah import BaseSekolah


def test_base_sekolah():
    assert issubclass(BaseSekolah, BaseDapodik)


def test_member():
    assert attr.has(AkreditasiSp)
    assert attr.has(BlockGrant)
    assert attr.has(JurusanSp)
    assert attr.has(Kepanitiaan)
    assert attr.has(ProgramInklusi)
    assert attr.has(Sanitasi)
    assert attr.has(SekolahLongitudinal)
    assert attr.has(SekolahPaud)
    assert attr.has(Sekolah)
    assert attr.has(Semester)
    assert attr.has(Yayasan)
