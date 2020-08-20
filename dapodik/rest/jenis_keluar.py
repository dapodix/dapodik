from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik.base import DapodikObject


@dataclass(eq=False)
class JenisKeluar(DapodikObject):
    jenis_keluar_id: str
    ket_keluar: str
    keluar_pd: str
    keluar_ptk: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
