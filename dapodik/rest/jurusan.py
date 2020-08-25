from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject, JenjangPendidikan
from dapodik.utils.decorator import set_meta


@set_meta('jurusan_id')
@dataclass(eq=False, frozen=True)
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

    @JenjangPendidikan.prop
    def jenjang_pendidikan(self) -> Optional[JenjangPendidikan]:
        return self.jenjang_pendidikan_id  # type: ignore

    @property
    def level_bidang(self):
        return self.level_bidang_id
