from dataclasses import dataclass
from datetime import datetime, date
from typing import Optional
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta('kurikulum_id')
@dataclass(eq=False, frozen=True)
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
