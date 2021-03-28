import attr
from datetime import datetime
from typing import Optional


@attr.dataclass(frozen=True, slots=True)
class Jurusan:
    jurusan_id: int
    nama_jurusan: str
    untuk_sma: str
    untuk_smk: str
    untuk_pt: str
    untuk_slb: str
    untuk_smklb: str
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

    def __str__(self):
        return self.nama_jurusan
