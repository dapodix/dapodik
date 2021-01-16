from datetime import datetime
from typing import Optional

from dapodik.base import dataclass


@dataclass(frozen=True)
class JenjangPendidikan:
    jenjang_pendidikan_id: str
    nama: str
    jenjang_lembaga: str
    jenjang_orang: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
