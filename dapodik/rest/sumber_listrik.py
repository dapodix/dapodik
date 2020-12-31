import attr
from datetime import datetime
from dapodik import DapodikObject
from typing import Optional
from dapodik.utils.decorator import set_meta


@set_meta("sumber_listrik_id")
@attr.dataclass(frozen=True)
class SumberListrik(DapodikObject):
    sumber_listrik_id: str
    nama: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
