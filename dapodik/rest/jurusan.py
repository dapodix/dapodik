import attr
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject, JenjangPendidikan
from dapodik.utils.decorator import set_meta


@set_meta("jurusan_id", jenjang_pendidikan=JenjangPendidikan)
@attr.dataclass(frozen=True)
class Jurusan(DapodikObject):
    jurusan_id: str
    nama_jurusan: str
    untuk_sma: str
    untuk_smk: str
    untuk_pt: str
    untuk_slb: str
    untuk_smklb: str
    jenjang_pendidikan_id: Optional[str]
    jurusan_induk: Optional[str]
    level_bidang_id: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    @property
    def level_bidang(self):
        # TODO API
        return self.level_bidang_id
