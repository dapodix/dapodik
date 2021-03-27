from datetime import datetime, date
from typing import Optional
from uuid import UUID

from dapodik import __semester__
import attr


@attr.dataclass
class RombonganBelajar:
    rombongan_belajar_id: UUID
    id_ruang: UUID
    sekolah_id: UUID
    tingkat_pendidikan_id: str
    jurusan_sp_id: Optional[str]
    kurikulum_id: int
    nama: str
    ptk_id: UUID
    moving_class: str
    jenis_rombel: int
    sks: str
    tanggal_mulai: date
    tanggal_selesai: date
    kebutuhan_khusus_id: int
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: UUID
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
    jurusan_id: int
    jurusan_id_str: str
    tingkat_pendidikan_id_str: str
    semester_id: str = __semester__
