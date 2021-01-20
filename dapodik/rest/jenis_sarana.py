from datetime import datetime
from typing import Optional

from dapodik.base import dataclass


@dataclass(frozen=True, slots=True)
class JenisSarana:
    jenis_sarana_id: str
    nama: str
    kelompok: Optional[str]
    perlu_penempatan: int
    keterangan: str
    a_alat: int
    a_angkutan: int
    spm_qty_min_per_siswa: str
    spm_qty_min_per_sekolah: int
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
