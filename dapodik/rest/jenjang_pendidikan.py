import attr
from datetime import datetime
from typing import Optional


@attr.dataclass(frozen=True, slots=True)
class JenjangPendidikan:
    jenjang_pendidikan_id: int
    nama: str
    jenjang_lembaga: int
    jenjang_orang: int
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nama
