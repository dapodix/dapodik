import attr
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta("id_jenis_lk")
@attr.dataclass(frozen=True)
class JenisLk(DapodikObject):
    id_jenis_lk: str
    nm_jenis_lk: str
    ket_jenis_lk: Optional[str]
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
