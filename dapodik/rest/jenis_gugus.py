import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class JenisGugus:
    jenis_gugus_id: int
    jenis_gugus: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.jenis_gugus

    class Prop(BaseProp):
        @property
        def jenis_gugus(self) -> "JenisGugus":
            return self.dapodik._find(
                self.dapodik.jenis_gugus(),
                lambda x: x.jenis_gugus_id == getattr(self, "jenis_gugus_id"),
            )

        @jenis_gugus.setter
        def jenis_gugus(self, value: "JenisGugus"):
            new_jenis_gugus = self.dapodik._find(
                self.dapodik.jenis_gugus(),
                lambda x: x.jenis_gugus_id == value.jenis_gugus_id,
            )
            setattr(self, "jenis_gugus_id", new_jenis_gugus.jenis_gugus_id)
