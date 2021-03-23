import attr
from dapodik.base import BaseDapodik
from dapodik.sarpras import AlatDariBlockgrant
from dapodik.sarpras import AlatLongitudinal
from dapodik.sarpras import Alat
from dapodik.sarpras import AngkutanDariBlockgrant
from dapodik.sarpras import Angkutan
from dapodik.sarpras import BangunanDariBlockgrant
from dapodik.sarpras import BangunanLongitudinal
from dapodik.sarpras import Bangunan
from dapodik.sarpras import BukuLongitudinal
from dapodik.sarpras import Buku
from dapodik.sarpras import RuangLongitudinal
from dapodik.sarpras import Ruang
from dapodik.sarpras import TanahDariBlockgrant
from dapodik.sarpras import TanahLongitudinal
from dapodik.sarpras import Tanah
from dapodik.sarpras import BaseSarpras


def test_base_sarpras():
    assert issubclass(BaseSarpras, BaseDapodik)


def test_member():
    assert attr.has(AlatDariBlockgrant)
    assert attr.has(AlatLongitudinal)
    assert attr.has(Alat)
    assert attr.has(AngkutanDariBlockgrant)
    assert attr.has(Angkutan)
    assert attr.has(BangunanDariBlockgrant)
    assert attr.has(BangunanLongitudinal)
    assert attr.has(Bangunan)
    assert attr.has(BukuLongitudinal)
    assert attr.has(Buku)
    assert attr.has(RuangLongitudinal)
    assert attr.has(Ruang)
    assert attr.has(TanahDariBlockgrant)
    assert attr.has(TanahLongitudinal)
    assert attr.has(Tanah)
