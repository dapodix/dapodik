from datetime import datetime
from typing import Optional

import attr


@attr.dataclass(frozen=True, slots=True)
class JadwalPaud:
    jadwal_id: int
    nama: str
    kesehatan: str
    pamts: str
    ddtk: str
    freq_parenting: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nama
