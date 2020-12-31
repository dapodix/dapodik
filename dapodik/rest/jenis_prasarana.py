import attr
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta("jenis_prasarana_id")
@attr.dataclass(frozen=True)
class JenisPrasarana(DapodikObject):
    jenis_prasarana_id: int
    nama: str
    a_unit_organisasi: str
    a_tanah: str
    a_bangunan: str
    a_ruang: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
