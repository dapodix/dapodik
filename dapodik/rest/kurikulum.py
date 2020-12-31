import attr
from datetime import datetime, date
from typing import Optional
from dapodik import DapodikObject, Jurusan
from dapodik.utils.decorator import set_meta


@set_meta("kurikulum_id", jurusan=Jurusan)
@attr.dataclass(frozen=True)
class Kurikulum(DapodikObject):
    kurikulum_id: int
    nama_kurikulum: str
    mulai_berlaku: date
    sistem_sks: str
    total_sks: str
    jenjang_pendidikan_id: str
    jurusan_id: Optional[str]
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
    sek: str
