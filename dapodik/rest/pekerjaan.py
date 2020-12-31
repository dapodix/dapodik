import attr
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta("pekerjaan_id")
@attr.dataclass(frozen=True)
class Pekerjaan(DapodikObject):
    pekerjaan_id: int
    nama: str
    a_wirausaha: str
    a_pejabat_publik: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
