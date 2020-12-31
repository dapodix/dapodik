import attr
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta("jenis_tinggal_id")
@attr.dataclass(frozen=True)
class JenjangPendidikan(DapodikObject):
    jenjang_pendidikan_id: str
    nama: str
    jenjang_lembaga: str
    jenjang_orang: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
