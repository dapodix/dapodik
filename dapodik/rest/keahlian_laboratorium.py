import attr
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta("keahlian_laboratorium_id")
@attr.dataclass(frozen=True)
class KeahlianLaboratorium(DapodikObject):
    keahlian_laboratorium_id: int
    nama: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
