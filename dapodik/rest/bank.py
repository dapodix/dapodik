import attr
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta("id_bank")
@attr.dataclass(frozen=True)
class Bank(DapodikObject):
    id_bank: str
    nm_bank: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
