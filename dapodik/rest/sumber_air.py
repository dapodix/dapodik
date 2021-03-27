from datetime import datetime
from typing import Optional

import attr


@attr.dataclass(frozen=True, slots=True)
class SumberAir:
    sumber_air_id: int
    nama: str
    sumber_air: str
    sumber_minum: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nama
