from datetime import datetime
from typing import Optional

from dapodik.base import dataclass


@dataclass(frozen=True)
class Akreditasi:
    akreditasi_id: str
    nama: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
