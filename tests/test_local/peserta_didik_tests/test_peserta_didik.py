from datetime import datetime, date
from random import randint
from uuid import UUID

from dapodik import Dapodik
from dapodik.peserta_didik import PesertaDidik


class TestPesertaDidik:
    def test_get_peserta_didik(self, dapodik: Dapodik, sekolah_id):
        limit = randint(5, 10)
        peserta_didiks = dapodik.peserta_didik.peserta_didik(
            sekolah_id=sekolah_id, limit=limit
        )
        assert peserta_didiks.id == "peserta_didik_id"
        if peserta_didiks.results > limit:
            assert len(peserta_didiks) == limit
        else:
            assert len(peserta_didiks) <= limit
        for peserta_didik in peserta_didiks:
            self.peserta_didik_test(peserta_didik)

    def peserta_didik_test(self, pd: PesertaDidik):
        assert isinstance(pd, PesertaDidik)
        assert isinstance(pd.peserta_didik_id, UUID)
        assert isinstance(pd.nama, str)
        assert isinstance(pd.jenis_kelamin, str)
        assert isinstance(pd.nisn, str)
        assert isinstance(pd.nik, str)
        assert isinstance(pd.no_kk, str)
        assert isinstance(pd.tempat_lahir, str)
        assert isinstance(pd.tanggal_lahir, date)
        assert isinstance(pd.agama_id, int)
        assert isinstance(pd.kebutuhan_khusus_id, int)
        assert isinstance(pd.alamat_jalan, str)
        assert isinstance(pd.rt, int)
        assert isinstance(pd.rw, int)
        assert isinstance(pd.nama_dusun, str)
        assert isinstance(pd.desa_kelurahan, str)
        assert isinstance(pd.kode_wilayah, str)
        if pd.kode_pos is not None:
            assert isinstance(pd.kode_pos, int)
        assert isinstance(pd.lintang, str)
        assert isinstance(pd.bujur, str)
        assert isinstance(pd.jenis_tinggal_id, int)
        assert isinstance(pd.alat_transportasi_id, int)
        assert isinstance(pd.nik_ayah, str)
        assert isinstance(pd.nik_ibu, str)
        assert isinstance(pd.anak_keberapa, int)
        if pd.nik_wali is not None:
            assert isinstance(pd.nik_wali, str)
        if pd.nomor_telepon_rumah is not None:
            assert isinstance(pd.nomor_telepon_rumah, str)
        if pd.nomor_telepon_seluler is not None:
            assert isinstance(pd.nomor_telepon_seluler, str)
        if pd.email is not None:
            assert isinstance(pd.email, str)
        assert isinstance(pd.penerima_kps, int)
        if pd.no_kps is not None:
            assert isinstance(pd.no_kps, str)
        assert isinstance(pd.layak_pip, int)
        assert isinstance(pd.penerima_kip, int)
        if pd.no_kip is not None:
            assert isinstance(pd.no_kip, str)
        assert isinstance(pd.nm_kip, int)
        if pd.no_kks is not None:
            assert isinstance(pd.no_kks, str)
        assert isinstance(pd.reg_akta_lahir, str)
        if pd.id_layak_pip is not None:
            assert isinstance(pd.id_layak_pip, int)
        if pd.id_bank is not None:
            assert isinstance(pd.id_bank, int)
        if pd.rekening_bank is not None:
            assert isinstance(pd.rekening_bank, str)
        if pd.nama_kcp is not None:
            assert isinstance(pd.nama_kcp, str)
        if pd.rekening_atas_nama is not None:
            assert isinstance(pd.rekening_atas_nama, str)
        assert isinstance(pd.status_data, int)
        assert isinstance(pd.nama_ayah, str)
        assert isinstance(pd.tahun_lahir_ayah, int)
        assert isinstance(pd.jenjang_pendidikan_ayah, int)
        assert isinstance(pd.pekerjaan_id_ayah, int)
        assert isinstance(pd.penghasilan_id_ayah, int)
        assert isinstance(pd.kebutuhan_khusus_id_ayah, int)
        assert isinstance(pd.nama_ibu_kandung, str)
        assert isinstance(pd.tahun_lahir_ibu, int)
        assert isinstance(pd.jenjang_pendidikan_ibu, int)
        assert isinstance(pd.penghasilan_id_ibu, int)
        assert isinstance(pd.pekerjaan_id_ibu, int)
        assert isinstance(pd.kebutuhan_khusus_id_ibu, int)
        if pd.nama_wali is not None:
            assert isinstance(pd.nama_wali, str)
        assert isinstance(pd.tahun_lahir_wali, int)
        assert isinstance(pd.jenjang_pendidikan_wali, int)
        assert isinstance(pd.pekerjaan_id_wali, int)
        assert isinstance(pd.penghasilan_id_wali, int)
        assert isinstance(pd.kewarganegaraan, str)
        assert isinstance(pd.create_date, datetime)
        assert isinstance(pd.last_update, datetime)
        assert isinstance(pd.soft_delete, int)
        assert isinstance(pd.last_sync, datetime)
        assert isinstance(pd.updater_id, UUID)
        assert isinstance(pd.registrasi_id, UUID)
        if pd.jurusan_sp_id is not None:
            assert isinstance(pd.jurusan_sp_id, str)
        assert isinstance(pd.sekolah_id, UUID)
        assert isinstance(pd.jenis_pendaftaran_id, int)
        assert isinstance(pd.nipd, int)
        assert isinstance(pd.tanggal_masuk_sekolah, date)
        if pd.jenis_keluar_id is not None:
            assert isinstance(pd.jenis_keluar_id, int)
        if pd.tanggal_keluar is not None:
            assert isinstance(pd.tanggal_keluar, datetime)
        assert isinstance(pd.keterangan, str)
        if pd.no_skhun is not None:
            assert isinstance(pd.no_skhun, str)
        if pd.no_peserta_ujian is not None:
            assert isinstance(pd.no_peserta_ujian, str)
        if pd.no_seri_ijazah is not None:
            assert isinstance(pd.no_seri_ijazah, str)
        assert isinstance(pd.a_pernah_paud, int)
        assert isinstance(pd.a_pernah_tk, int)
        if pd.sekolah_asal is not None:
            assert isinstance(pd.sekolah_asal, str)
        assert isinstance(pd.id_hobby, int)
        assert isinstance(pd.id_cita, int)
        assert isinstance(pd.nama_sorter, str)
        assert isinstance(pd.jenis_pendaftaran_id_str, str)
        if pd.ket_keluar is not None:
            assert isinstance(pd.ket_keluar, str)
        if pd.anggota_rombel_id is not None:
            assert isinstance(pd.anggota_rombel_id, UUID)
        if pd.tingkat_pendidikan_id is not None:
            assert isinstance(pd.tingkat_pendidikan_id, int)
        assert isinstance(pd.rombel_saat_ini, str)
        assert isinstance(pd.rombel, str)
        if pd.id_bank_str is not None:
            assert isinstance(pd.id_bank_str, str)
        assert isinstance(pd.kewarganegaraan_str, str)
        assert isinstance(pd.nomor_induk_pd, int)
        assert isinstance(pd.yatim_piatu, bool)
        assert isinstance(pd.konfirmasi_mutasi, int)
        assert isinstance(pd.vld_count, int)
