from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik.base import DapodikObject


@dataclass(eq=False)
class RombonganBelajar(DapodikObject):
    rombongan_belajar_id: str
    semester_id: str
    id_ruang: str
    sekolah_id: str
    tingkat_pendidikan_id: str
    jurusan_sp_id: Optional[str]
    kurikulum_id: int
    nama: str
    ptk_id: str
    moving_class: str
    jenis_rombel: str
    sks: str
    tanggal_mulai: str
    tanggal_selesai: str
    kebutuhan_khusus_id: int
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    semester_id_str: str
    sekolah_id_str: str
    kurikulum_id_str: str
    ptk_id_str: str
    id_ruang_str: str
    kebutuhan_khusus_id_str: str
    vld_count: int
    pembelajaran_count: int
    anggota_rombel_count: int
    jenis_rombel_str: str
    jurusan_id: str
    jurusan_id_str: str
