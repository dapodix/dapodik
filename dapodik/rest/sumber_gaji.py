import attr
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta("sumber_gaji_id")
@attr.dataclass(frozen=True)
class SumberGaji(DapodikObject):
    sumber_gaji_id: str
    nama: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
