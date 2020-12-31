import attr
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta("akses_internet_id")
@attr.dataclass(frozen=True)
class AksesInternet(DapodikObject):
    akses_internet_id: int
    nama: str
    media: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
