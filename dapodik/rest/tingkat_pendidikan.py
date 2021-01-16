from datetime import datetime
from typing import Optional

from dapodik.base import dataclass


@dataclass(frozen=True)
class TingkatPendidikan:
    tingkat_pendidikan_id: str
    kode: str
    nama: str
    jenjang_pendidikan_id: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
