from dapodik import Dapodik
from dapodik.base import Results
from dapodik.sarpras import (
    AlatDariBlockgrant,
    AlatLongitudinal,
    Alat,
    AngkutanDariBlockgrant,
    Angkutan,
    BangunanDariBlockgrant,
    BangunanLongitudinal,
    Bangunan,
    BukuLongitudinal,
    Buku,
    RuangLongitudinal,
    Ruang,
    TanahDariBlockgrant,
    TanahLongitudinal,
    Tanah,
)


class TestSarpras:
    def test_alat_dari_blockgrant(self, dapodik: Dapodik):
        data = dapodik.sarpras.alat_dari_blockgrant()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, AlatDariBlockgrant)

    def test_alat_longitudinal(self, dapodik: Dapodik):
        data = dapodik.sarpras.alat_longitudinal()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, AlatLongitudinal)

    def test_alat(self, dapodik: Dapodik):
        data = dapodik.sarpras.alat()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, Alat)

    def test_angkutan_dari_blockgrant(self, dapodik: Dapodik):
        data = dapodik.sarpras.angkutan_dari_blockgrant()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, AngkutanDariBlockgrant)

    def test_angkutan(self, dapodik: Dapodik):
        data = dapodik.sarpras.angkutan()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, Angkutan)

    def test_bangunan_dari_blockgrant(self, dapodik: Dapodik):
        data = dapodik.sarpras.bangunan_dari_blockgrant()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, BangunanDariBlockgrant)

    def test_bangunan_longitudinal(self, dapodik: Dapodik):
        data = dapodik.sarpras.bangunan_longitudinal()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, BangunanLongitudinal)

    def test_bangunan(self, dapodik: Dapodik):
        data = dapodik.sarpras.bangunan()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, Bangunan)

    def test_buku_longitudinal(self, dapodik: Dapodik):
        data = dapodik.sarpras.buku_longitudinal()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, BukuLongitudinal)

    def test_buku(self, dapodik: Dapodik):
        data = dapodik.sarpras.buku()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, Buku)

    def test_ruang_longitudinal(self, dapodik: Dapodik):
        data = dapodik.sarpras.ruang_longitudinal()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, RuangLongitudinal)

    def test_ruang(self, dapodik: Dapodik):
        data = dapodik.sarpras.ruang()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, Ruang)

    def test_tanah_dari_blockgrant(self, dapodik: Dapodik):
        data = dapodik.sarpras.tanah_dari_blockgrant()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, TanahDariBlockgrant)

    def test_tanah_longitudinal(self, dapodik: Dapodik):
        data = dapodik.sarpras.tanah_longitudinal()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, TanahLongitudinal)

    def test_tanah(self, dapodik: Dapodik):
        data = dapodik.sarpras.tanah()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, Tanah)
