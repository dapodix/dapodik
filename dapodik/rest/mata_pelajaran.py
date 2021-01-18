from datetime import datetime
from typing import Optional

from dapodik.base import dataclass


@dataclass(frozen=True, slots=True)
class MataPelajaran:
    mata_pelajaran_id: int
    nama: str
    pilihan_sekolah: str
    pilihan_buku: str
    pilihan_kepengawasan: str
    pilihan_evaluasi: str
    jurusan_id: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nama
