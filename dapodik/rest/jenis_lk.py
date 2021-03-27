import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class JenisLk:
    id_jenis_lk: str
    nm_jenis_lk: str
    ket_jenis_lk: Optional[str]
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nm_jenis_lk

    class Prop(BaseProp):
        @property
        def jenis_lk(self) -> "JenisLk":
            return self.dapodik._find(
                self.dapodik.jenis_lk(),
                lambda x: x.id_jenis_lk == getattr(self, "id_jenis_lk"),
            )

        @jenis_lk.setter
        def jenis_lk(self, value: "JenisLk"):
            new_jenis_lk = self.dapodik._find(
                self.dapodik.jenis_lk(),
                lambda x: x.id_jenis_lk == value.id_jenis_lk,
            )
            setattr(self, "id_jenis_lk", new_jenis_lk.id_jenis_lk)
