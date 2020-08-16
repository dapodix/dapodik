from dataclasses import dataclass
from typing import Optional
from dapodik.base import BaseData


@dataclass
class WaktuPenyelenggaraan(BaseData):
    waktu_penyelenggaraan_id: str
    nama: str
    create_date: str
    last_update: str
    expired_date: Optional[str]
    last_sync: str
