import attr
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta("tingkat_pendidikan_id")
@attr.dataclass(frozen=True)
class TingkatPendidikan(DapodikObject):
    tingkat_pendidikan_id: str
    kode: str
    nama: str
    jenjang_pendidikan_id: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
