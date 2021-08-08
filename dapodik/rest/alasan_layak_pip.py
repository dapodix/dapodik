import attr
from datetime import datetime
from typing import Optional


@attr.dataclass(frozen=True, slots=True)
class AlasanLayakPip:
    id_layak_pip: int
    alasan_layak_pip: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.alasan_layak_pip
