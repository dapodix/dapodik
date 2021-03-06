from dapodik import Dapodik
from dapodik.validasi import (
    Validasi,
    ValidasiSekolah,
    ValidasiPrasarana,
    ValidasiPesertaDidik,
    ValidasiPtk,
    ValidasiRombonganBelajar,
    ValidasiPembelajaran,
    ValidasiNilai,
    ValidasiReferensi,
)


class TestValidasi:
    def test_get_validasi_sekolah(self, dapodik: Dapodik):
        validasi = dapodik.validasi_sekolah()
        assert isinstance(len(validasi), int)
        assert validasi.id == "validasi_id"
        for valid in validasi:
            assert isinstance(valid, Validasi)
            assert isinstance(valid, ValidasiSekolah)
            assert isinstance(valid.validasi_id, int)
            assert isinstance(valid.table, str)
            assert isinstance(valid.tipe, int)
            assert isinstance(valid.keterangan, str)

    def test_get_validasi_prasarana(self, dapodik: Dapodik):
        validasi = dapodik.validasi_prasarana()
        assert isinstance(len(validasi), int)
        assert validasi.id == "validasi_id"
        for valid in validasi:
            assert isinstance(valid, Validasi)
            assert isinstance(valid, ValidasiPrasarana)
            assert isinstance(valid.validasi_id, int)
            assert isinstance(valid.table, str)
            assert isinstance(valid.tipe, int)
            assert isinstance(valid.keterangan, str)

    def test_get_validasi_peserta_didik(self, dapodik: Dapodik):
        validasi = dapodik.validasi_peserta_didik()
        assert isinstance(len(validasi), int)
        assert validasi.id == "validasi_id"
        for valid in validasi:
            assert isinstance(valid, Validasi)
            assert isinstance(valid, ValidasiPesertaDidik)
            assert isinstance(valid.validasi_id, int)
            assert isinstance(valid.table, str)
            assert isinstance(valid.tipe, int)
            assert isinstance(valid.keterangan, str)

    def test_get_validasi_ptk(self, dapodik: Dapodik):
        validasi = dapodik.validasi_ptk()
        assert isinstance(len(validasi), int)
        assert validasi.id == "validasi_id"
        for valid in validasi:
            assert isinstance(valid, Validasi)
            assert isinstance(valid, ValidasiPtk)
            assert isinstance(valid.validasi_id, int)
            assert isinstance(valid.table, str)
            assert isinstance(valid.tipe, int)
            assert isinstance(valid.keterangan, str)

    def test_get_validasi_rombongan_belajar(self, dapodik: Dapodik):
        validasi = dapodik.validasi_rombongan_belajar()
        assert isinstance(len(validasi), int)
        assert validasi.id == "validasi_id"
        for valid in validasi:
            assert isinstance(valid, Validasi)
            assert isinstance(valid, ValidasiRombonganBelajar)
            assert isinstance(valid.validasi_id, int)
            assert isinstance(valid.table, str)
            assert isinstance(valid.tipe, int)
            assert isinstance(valid.keterangan, str)

    def test_get_validasi_pembelajaran(self, dapodik: Dapodik):
        validasi = dapodik.validasi_pembelajaran()
        assert isinstance(len(validasi), int)
        assert validasi.id == "validasi_id"
        for valid in validasi:
            assert isinstance(valid, Validasi)
            assert isinstance(valid, ValidasiPembelajaran)
            assert isinstance(valid.validasi_id, int)
            assert isinstance(valid.table, str)
            assert isinstance(valid.tipe, int)
            assert isinstance(valid.keterangan, str)

    def test_get_validasi_nilai(self, dapodik: Dapodik):
        validasi = dapodik.validasi_nilai()
        assert isinstance(len(validasi), int)
        assert validasi.id == "validasi_id"
        for valid in validasi:
            assert isinstance(valid, Validasi)
            assert isinstance(valid, ValidasiNilai)
            assert isinstance(valid.validasi_id, int)
            assert isinstance(valid.table, str)
            assert isinstance(valid.tipe, int)
            assert isinstance(valid.keterangan, str)

    def test_get_validasi_referensi(self, dapodik: Dapodik):
        validasi = dapodik.validasi_referensi()
        assert isinstance(len(validasi), int)
        assert validasi.id == "validasi_id"
        for valid in validasi:
            assert isinstance(valid, Validasi)
            assert isinstance(valid, ValidasiReferensi)
            assert isinstance(valid.validasi_id, int)
            assert isinstance(valid.table, str)
            assert isinstance(valid.tipe, int)
            assert isinstance(valid.keterangan, str)
