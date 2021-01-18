from datetime import datetime, date
from typing import Optional
from uuid import UUID

from dapodik import __semester__
from dapodik.base import dataclass, freeze


@dataclass
class RombonganBelajar:
    rombongan_belajar_id: UUID = freeze(default=None)
    semester_id: str = freeze(default=__semester__)
    id_ruang: UUID
    sekolah_id: UUID = freeze(default=None)
    tingkat_pendidikan_id: str
    jurusan_sp_id: Optional[str] = freeze(default=None)
    kurikulum_id: int = 301
    nama: str
    ptk_id: UUID
    moving_class: str
    jenis_rombel: str
    sks: str = "0"
    tanggal_mulai: date = freeze(default=None)
    tanggal_selesai: date = freeze(default=None)
    kebutuhan_khusus_id: int
    create_date: datetime = freeze(default=None)
    last_update: datetime = freeze(default=None)
    soft_delete: str = freeze(default=None)
    last_sync: datetime = freeze(default=None)
    updater_id: UUID = freeze(default=None)
    semester_id_str: str = freeze(default=None)
    sekolah_id_str: str = freeze(default=None)
    kurikulum_id_str: str = freeze(default=None)
    ptk_id_str: str = freeze(default=None)
    id_ruang_str: str = freeze(default=None)
    kebutuhan_khusus_id_str: str = freeze(default=None)
    vld_count: int = freeze(default=None)
    pembelajaran_count: int = freeze(default=None)
    anggota_rombel_count: int = freeze(default=None)
    jenis_rombel_str: str = freeze(default=None)
    jurusan_id: str
    jurusan_id_str: str = freeze(default=None)
    tingkat_pendidikan_id_str: str = freeze(default=None)
