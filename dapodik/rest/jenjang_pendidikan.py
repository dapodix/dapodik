from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik.base import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta('jenis_tinggal_id')
@dataclass(eq=False)
class JenjangPendidikan(DapodikObject):
    jenjang_pendidikan_id: str
    nama: str
    jenjang_lembaga: str
    jenjang_orang: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
