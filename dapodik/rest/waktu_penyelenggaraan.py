from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik.base import DapodikObject


@dataclass(eq=False)
class WaktuPenyelenggaraan(DapodikObject):
    waktu_penyelenggaraan_id: str
    nama: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
    _id: str = 'waktu_penyelenggaraan_id'
