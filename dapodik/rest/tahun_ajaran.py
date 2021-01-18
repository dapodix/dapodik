from datetime import datetime, date
from typing import Optional

from dapodik.base import dataclass


@dataclass(frozen=True, slots=True)
class TahunAjaran:
    tahun_ajaran_id: str
    nama: str
    periode_aktif: str
    tanggal_mulai: date
    tanggal_selesai: date
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nama
