import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class JenjangPendidikan:
    jenjang_pendidikan_id: int
    nama: str
    jenjang_lembaga: int
    jenjang_orang: int
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nama

    class Prop(BaseProp):
        @property
        def jenjang_pendidikan(self) -> "JenjangPendidikan":
            return self.dapodik._find(
                self.dapodik.jenjang_pendidikan(),
                lambda x: x.jenjang_pendidikan_id
                == getattr(self, "jenjang_pendidikan_id"),
            )

        @jenjang_pendidikan.setter
        def jenjang_pendidikan(self, value: "JenjangPendidikan"):
            new = self.dapodik._find(
                self.dapodik.jenjang_pendidikan(),
                lambda x: x.jenjang_pendidikan_id == value.jenjang_pendidikan_id,
            )
            setattr(self, "jenjang_pendidikan_id", new.jenjang_pendidikan_id)
