from datetime import datetime, date
from typing import Optional

from dapodik.base import dataclass


@dataclass(frozen=True, slots=True)
class Kurikulum:
    kurikulum_id: int
    nama_kurikulum: str
    mulai_berlaku: date
    sistem_sks: str
    total_sks: str
    jenjang_pendidikan_id: str
    jurusan_id: Optional[str]
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
    sek: str

    def __str__(self):
        return self.nama_kurikulum
