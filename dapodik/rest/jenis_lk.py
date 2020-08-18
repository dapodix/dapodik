from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik.base import BaseData


@dataclass
class JenisLk(BaseData):
    id_jenis_lk: str
    nm_jenis_lk: str
    ket_jenis_lk: Optional[str]
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
