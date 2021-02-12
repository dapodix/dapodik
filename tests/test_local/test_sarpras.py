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
        data = dapodik.alat_dari_blockgrant()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, AlatDariBlockgrant)

    def test_alat_longitudinal(self, dapodik: Dapodik):
        data = dapodik.alat_longitudinal()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, AlatLongitudinal)

    def test_alat(self, dapodik: Dapodik):
        data = dapodik.alat()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, Alat)

    def test_angkutan_dari_blockgrant(self, dapodik: Dapodik):
        data = dapodik.angkutan_dari_blockgrant()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, AngkutanDariBlockgrant)

    def test_angkutan(self, dapodik: Dapodik):
        data = dapodik.angkutan()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, Angkutan)

    def test_bangunan_dari_blockgrant(self, dapodik: Dapodik):
        data = dapodik.bangunan_dari_blockgrant()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, BangunanDariBlockgrant)

    def test_bangunan_longitudinal(self, dapodik: Dapodik):
        data = dapodik.bangunan_longitudinal()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, BangunanLongitudinal)

    def test_bangunan(self, dapodik: Dapodik):
        data = dapodik.bangunan()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, Bangunan)

    def test_buku_longitudinal(self, dapodik: Dapodik):
        data = dapodik.buku_longitudinal()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, BukuLongitudinal)

    def test_buku(self, dapodik: Dapodik):
        data = dapodik.buku()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, Buku)

    def test_ruang_longitudinal(self, dapodik: Dapodik):
        data = dapodik.ruang_longitudinal()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, RuangLongitudinal)

    def test_ruang(self, dapodik: Dapodik):
        data = dapodik.ruang()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, Ruang)

    def test_tanah_dari_blockgrant(self, dapodik: Dapodik):
        data = dapodik.tanah_dari_blockgrant()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, TanahDariBlockgrant)

    def test_tanah_longitudinal(self, dapodik: Dapodik):
        data = dapodik.tanah_longitudinal()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, TanahLongitudinal)

    def test_tanah(self, dapodik: Dapodik):
        data = dapodik.tanah()
        assert isinstance(data, Results)
        for dat in data:
            assert isinstance(dat, Tanah)
