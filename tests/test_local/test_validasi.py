from dapodik import Dapodik
from dapodik.validasi import Validasi


class TestValidasi:
    def test_get_validasi_sekolah(self, dapodik: Dapodik):
        validasi = dapodik.validasi.sekolah()
        assert isinstance(len(validasi), int)
        assert validasi.id == "validasi_id"
        for valid in validasi:
            assert isinstance(valid, Validasi)
            assert isinstance(valid.validasi_id, int)
            assert isinstance(valid.table, str)
            assert isinstance(valid.tipe, int)
            assert isinstance(valid.keterangan, str)

    def test_get_validasi_prasarana(self, dapodik: Dapodik):
        validasi = dapodik.validasi.prasarana()
        assert isinstance(len(validasi), int)
        assert validasi.id == "validasi_id"
        for valid in validasi:
            assert isinstance(valid, Validasi)
            assert isinstance(valid.validasi_id, int)
            assert isinstance(valid.table, str)
            assert isinstance(valid.tipe, int)
            assert isinstance(valid.keterangan, str)

    def test_get_validasi_peserta_didik(self, dapodik: Dapodik):
        validasi = dapodik.validasi.peserta_didik()
        assert isinstance(len(validasi), int)
        assert validasi.id == "validasi_id"
        for valid in validasi:
            assert isinstance(valid, Validasi)
            assert isinstance(valid.validasi_id, int)
            assert isinstance(valid.table, str)
            assert isinstance(valid.tipe, int)
            assert isinstance(valid.keterangan, str)

    def test_get_validasi_ptk(self, dapodik: Dapodik):
        validasi = dapodik.validasi.ptk()
        assert isinstance(len(validasi), int)
        assert validasi.id == "validasi_id"
        for valid in validasi:
            assert isinstance(valid, Validasi)
            assert isinstance(valid.validasi_id, int)
            assert isinstance(valid.table, str)
            assert isinstance(valid.tipe, int)
            assert isinstance(valid.keterangan, str)

    def test_get_validasi_rombongan_belajar(self, dapodik: Dapodik):
        validasi = dapodik.validasi.rombongan_belajar()
        assert isinstance(len(validasi), int)
        assert validasi.id == "validasi_id"
        for valid in validasi:
            assert isinstance(valid, Validasi)
            assert isinstance(valid.validasi_id, int)
            assert isinstance(valid.table, str)
            assert isinstance(valid.tipe, int)
            assert isinstance(valid.keterangan, str)

    def test_get_validasi_pembelajaran(self, dapodik: Dapodik):
        validasi = dapodik.validasi.pembelajaran()
        assert isinstance(len(validasi), int)
        assert validasi.id == "validasi_id"
        for valid in validasi:
            assert isinstance(valid, Validasi)
            assert isinstance(valid.validasi_id, int)
            assert isinstance(valid.table, str)
            assert isinstance(valid.tipe, int)
            assert isinstance(valid.keterangan, str)

    def test_get_validasi_nilai(self, dapodik: Dapodik):
        validasi = dapodik.validasi.nilai()
        assert isinstance(len(validasi), int)
        assert validasi.id == "validasi_id"
        for valid in validasi:
            assert isinstance(valid, Validasi)
            assert isinstance(valid.validasi_id, int)
            assert isinstance(valid.table, str)
            assert isinstance(valid.tipe, int)
            assert isinstance(valid.keterangan, str)

    def test_get_validasi_referensi(self, dapodik: Dapodik):
        validasi = dapodik.validasi.referensi()
        assert isinstance(len(validasi), int)
        assert validasi.id == "validasi_id"
        for valid in validasi:
            assert isinstance(valid, Validasi)
            assert isinstance(valid.validasi_id, int)
            assert isinstance(valid.table, str)
            assert isinstance(valid.tipe, int)
            assert isinstance(valid.keterangan, str)
