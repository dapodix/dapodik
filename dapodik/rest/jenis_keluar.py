import attr
from datetime import datetime
from typing import Optional


@attr.dataclass(frozen=True, slots=True)
class JenisKeluar:
    jenis_keluar_id: int
    ket_keluar: str
    keluar_pd: str
    keluar_ptk: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.ket_keluar
