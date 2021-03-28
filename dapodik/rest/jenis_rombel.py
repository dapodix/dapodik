import attr
from datetime import datetime
from typing import Optional


@attr.dataclass(frozen=True, slots=True)
class JenisRombel:
    jenis_rombel: int
    nm_jenis_rombel: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nm_jenis_rombel
