from datetime import datetime, date

from dapodik import Dapodik
from dapodik.sekolah import Sekolah


class TestSekolah:
    def test_get_sekolah(self, dapodik: Dapodik):
        s = dapodik.sekolah.sekolah()
        assert isinstance(s, Sekolah)
        assert isinstance(s.sekolah_id, str)
        assert isinstance(s.nama, str)
        if s.nama_nomenklatur:
            assert isinstance(s.nama_nomenklatur, str)
        assert isinstance(s.nss, str)
        assert isinstance(s.npsn, str)
        assert isinstance(s.bentuk_pendidikan_id, int)
        assert isinstance(s.alamat_jalan, str)
        if s.rt:
            assert isinstance(s.rt, str)
        if s.rw:
            assert isinstance(s.rw, str)
        if s.nama_dusun:
            assert isinstance(s.nama_dusun, str)
        assert isinstance(s.desa_kelurahan, str)
        assert isinstance(s.kode_wilayah, str)
        if s.kode_pos:
            assert isinstance(s.kode_pos, str)
        if s.lintang:
            assert isinstance(s.lintang, str)
        if s.bujur:
            assert isinstance(s.bujur, str)
        if s.nomor_telepon:
            assert isinstance(s.nomor_telepon, str)
        if s.nomor_fax:
            assert isinstance(s.nomor_fax, str)
        if s.email:
            assert isinstance(s.email, str)
        if s.website:
            assert isinstance(s.website, str)
        assert isinstance(s.kebutuhan_khusus_id, int)
        assert isinstance(s.status_sekolah, str)
        assert isinstance(s.sk_pendirian_sekolah, str)
        assert isinstance(s.tanggal_sk_pendirian, date)
        assert isinstance(s.status_kepemilikan_id, str)
        assert isinstance(s.yayasan_id, str)
        assert isinstance(s.sk_izin_operasional, str)
        assert isinstance(s.tanggal_sk_izin_operasional, date)
        if s.no_rekening:
            assert isinstance(s.no_rekening, str)
        if s.nama_bank:
            assert isinstance(s.nama_bank, str)
        if s.cabang_kcp_unit:
            assert isinstance(s.cabang_kcp_unit, str)
        if s.rekening_atas_nama:
            assert isinstance(s.rekening_atas_nama, str)
        assert isinstance(s.mbs, str)
        assert isinstance(s.luas_tanah_milik, str)
        assert isinstance(s.luas_tanah_bukan_milik, str)
        assert isinstance(s.kode_registrasi, str)
        if s.npwp:
            assert isinstance(s.npwp, str)
        if s.nm_wp:
            assert isinstance(s.nm_wp, str)
        assert isinstance(s.keaktifan, str)
        if s.flag:
            assert isinstance(s.flag, str)
        assert isinstance(s.create_date, datetime)
        assert isinstance(s.last_update, datetime)
        assert isinstance(s.soft_delete, str)
        assert isinstance(s.last_sync, datetime)
        assert isinstance(s.updater_id, str)
        assert isinstance(s.bentuk_pendidikan_id_str, str)
        assert isinstance(s.kode_wilayah_str, str)
        assert isinstance(s.kebutuhan_khusus_id_str, str)
        assert isinstance(s.yayasan_id_str, str)
        assert isinstance(s.vld_count, int)
