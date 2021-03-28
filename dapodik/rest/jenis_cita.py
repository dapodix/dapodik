import attr
from datetime import datetime
from typing import Optional


@attr.dataclass(frozen=True, slots=True)
class JenisCita:
    id_cita: int
    nm_cita: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nm_cita
