from datetime import datetime, date
from unittest import TestCase

from dapodik import Dapodik
from dapodik.sekolah import Sekolah


class TestSekolah(TestCase):
    def get_sekolah_test(self, dapodik: Dapodik):
        s = dapodik.sekolah.sekolah()
        assert isinstance(s, Sekolah)
        self.assertIsInstance(s.sekolah_id, str)
        self.assertIsInstance(s.nama, str)
        if s.nama_nomenklatur:
            self.assertIsInstance(s.nama_nomenklatur, str)
        self.assertIsInstance(s.nss, str)
        self.assertIsInstance(s.npsn, str)
        self.assertIsInstance(s.bentuk_pendidikan_id, int)
        self.assertIsInstance(s.alamat_jalan, str)
        if s.rt:
            self.assertIsInstance(s.rt, str)
        if s.rw:
            self.assertIsInstance(s.rw, str)
        if s.nama_dusun:
            self.assertIsInstance(s.nama_dusun, str)
        self.assertIsInstance(s.desa_kelurahan, str)
        self.assertIsInstance(s.kode_wilayah, str)
        if s.kode_pos:
            self.assertIsInstance(s.kode_pos, str)
        if s.lintang:
            self.assertIsInstance(s.lintang, str)
        if s.bujur:
            self.assertIsInstance(s.bujur, str)
        if s.nomor_telepon:
            self.assertIsInstance(s.nomor_telepon, str)
        if s.nomor_fax:
            self.assertIsInstance(s.nomor_fax, str)
        if s.email:
            self.assertIsInstance(s.email, str)
        if s.website:
            self.assertIsInstance(s.website, str)
        self.assertIsInstance(s.kebutuhan_khusus_id, int)
        self.assertIsInstance(s.status_sekolah, str)
        self.assertIsInstance(s.sk_pendirian_sekolah, str)
        self.assertIsInstance(s.tanggal_sk_pendirian, date)
        self.assertIsInstance(s.status_kepemilikan_id, str)
        self.assertIsInstance(s.yayasan_id, str)
        self.assertIsInstance(s.sk_izin_operasional, str)
        self.assertIsInstance(s.tanggal_sk_izin_operasional, date)
        if s.no_rekening:
            self.assertIsInstance(s.no_rekening, str)
        if s.nama_bank:
            self.assertIsInstance(s.nama_bank, str)
        if s.cabang_kcp_unit:
            self.assertIsInstance(s.cabang_kcp_unit, str)
        if s.rekening_atas_nama:
            self.assertIsInstance(s.rekening_atas_nama, str)
        self.assertIsInstance(s.mbs, str)
        self.assertIsInstance(s.luas_tanah_milik, str)
        self.assertIsInstance(s.luas_tanah_bukan_milik, str)
        self.assertIsInstance(s.kode_registrasi, str)
        if s.npwp:
            self.assertIsInstance(s.npwp, str)
        if s.nm_wp:
            self.assertIsInstance(s.nm_wp, str)
        self.assertIsInstance(s.keaktifan, str)
        if s.flag:
            self.assertIsInstance(s.flag, str)
        self.assertIsInstance(s.create_date, datetime)
        self.assertIsInstance(s.last_update, datetime)
        self.assertIsInstance(s.soft_delete, str)
        self.assertIsInstance(s.last_sync, datetime)
        self.assertIsInstance(s.updater_id, str)
        self.assertIsInstance(s.bentuk_pendidikan_id_str, str)
        self.assertIsInstance(s.kode_wilayah_str, str)
        self.assertIsInstance(s.kebutuhan_khusus_id_str, str)
        self.assertIsInstance(s.yayasan_id_str, str)
        self.assertIsInstance(s.vld_count, int)
