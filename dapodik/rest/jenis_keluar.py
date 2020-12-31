import attr
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta("jenis_keluar_id")
@attr.dataclass(frozen=True)
class JenisKeluar(DapodikObject):
    jenis_keluar_id: str
    ket_keluar: str
    keluar_pd: str
    keluar_ptk: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
