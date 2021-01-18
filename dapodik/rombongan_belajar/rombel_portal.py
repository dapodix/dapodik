from datetime import datetime
from typing import Optional
from uuid import UUID

from dapodik.base import dataclass


@dataclass(frozen=True, slots=True)
class RombelPortal:
    rombongan_belajar_id: UUID
    semester_id: int
    id_ruang: UUID
    sekolah_id: UUID
    tingkat_pendidikan_id: int
    jurusan_sp_id: Optional[str]
    kurikulum_id: int
    nama: str
    ptk_id: UUID
    moving_class: int
    jenis_rombel: int
    sks: int
    tanggal_mulai: datetime
    tanggal_selesai: datetime
    kebutuhan_khusus_id: int
    create_date: datetime
    last_update: datetime
    soft_delete: int
    last_sync: datetime
    updater_id: UUID
    no: int
    laki_laki: int
    perempuan: int
    keluar: int
    mutasi: int
    do: int
    jumlah: int
