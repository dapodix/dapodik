from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik.base import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta('pekerjaan_id')
@dataclass(eq=False)
class Pekerjaan(DapodikObject):
    pekerjaan_id: int
    nama: str
    a_wirausaha: str
    a_pejabat_publik: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
