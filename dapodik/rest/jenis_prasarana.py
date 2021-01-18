from datetime import datetime
from typing import Optional

from dapodik.base import dataclass


@dataclass(frozen=True, slots=True)
class JenisPrasarana:
    jenis_prasarana_id: int
    nama: str
    a_unit_organisasi: str
    a_tanah: str
    a_bangunan: str
    a_ruang: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nama
