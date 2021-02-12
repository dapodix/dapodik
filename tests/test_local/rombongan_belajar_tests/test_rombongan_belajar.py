from datetime import datetime, date
from uuid import UUID

from dapodik import Dapodik
from dapodik.rombongan_belajar import RombonganBelajar


class TestRombonganBelajar:
    def test_get_rombongan_belajar(
        self, dapodik: Dapodik, sekolah_id: str, semester: str
    ):
        rombongan_belajar = dapodik.rombongan_belajar(
            sekolah_id=sekolah_id, semester_id=semester
        )
        for ro in rombongan_belajar:
            assert isinstance(ro, RombonganBelajar)
            assert isinstance(ro.rombongan_belajar_id, UUID)
            assert isinstance(ro.semester_id, str)
            assert isinstance(ro.id_ruang, UUID)
            assert isinstance(ro.sekolah_id, UUID)
            assert isinstance(ro.tingkat_pendidikan_id, str)
            if ro.jurusan_sp_id is not None:
                assert isinstance(ro.jurusan_sp_id, str)
            assert isinstance(ro.kurikulum_id, int)
            assert isinstance(ro.nama, str)
            assert isinstance(ro.ptk_id, UUID)
            assert isinstance(ro.moving_class, str)
            assert isinstance(ro.jenis_rombel, str)
            assert isinstance(ro.sks, str)
            assert isinstance(ro.tanggal_mulai, date)
            assert isinstance(ro.tanggal_selesai, date)
            assert isinstance(ro.kebutuhan_khusus_id, int)
            assert isinstance(ro.create_date, datetime)
            assert isinstance(ro.last_update, datetime)
            assert isinstance(ro.soft_delete, str)
            assert isinstance(ro.last_sync, datetime)
            assert isinstance(ro.updater_id, UUID)
            assert isinstance(ro.semester_id_str, str)
            assert isinstance(ro.sekolah_id_str, str)
            assert isinstance(ro.kurikulum_id_str, str)
            assert isinstance(ro.ptk_id_str, str)
            assert isinstance(ro.id_ruang_str, str)
            assert isinstance(ro.kebutuhan_khusus_id_str, str)
            assert isinstance(ro.vld_count, int)
            assert isinstance(ro.pembelajaran_count, int)
            assert isinstance(ro.anggota_rombel_count, int)
            assert isinstance(ro.jenis_rombel_str, str)
            assert isinstance(ro.jurusan_id, str)
            assert isinstance(ro.jurusan_id_str, str)
            assert isinstance(ro.tingkat_pendidikan_id_str, str)
