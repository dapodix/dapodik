import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


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

    class Prop(BaseProp):
        @property
        def jurusan(self) -> "Jurusan":
            return self.dapodik._find(
                self.dapodik.jurusan(),
                lambda x: x.jurusan_id == getattr(self, "jurusan_id"),
            )

        @jurusan.setter
        def jurusan(self, value: "Jurusan"):
            new = self.dapodik._find(
                self.dapodik.jurusan(),
                lambda x: x.jurusan_id == value.jurusan_id,
            )
            setattr(self, "jurusan_id", new.jurusan_id)
