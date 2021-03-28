import attr
from datetime import datetime
from typing import Optional


@attr.dataclass(frozen=True, slots=True)
class Bank:
    id_bank: str
    nm_bank: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nm_bank
