from datetime import datetime
from typing import Optional

from dapodik.base import dataclass


@dataclass(frozen=True, slots=True)
class JenisRombel:
    jenis_rombel: str
    nm_jenis_rombel: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nm_jenis_rombel
