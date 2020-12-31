import attr
from datetime import datetime, date
from typing import Optional
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta("tahun_ajaran_id")
@attr.dataclass(frozen=True)
class TahunAjaran(DapodikObject):
    tahun_ajaran_id: str
    nama: str
    periode_aktif: str
    tanggal_mulai: date
    tanggal_selesai: date
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
