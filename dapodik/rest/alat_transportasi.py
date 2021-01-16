from datetime import datetime
from typing import Optional

from dapodik.base import dataclass


@dataclass(frozen=True)
class AlatTransportasi:
    alat_transportasi_id: str
    nama: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
