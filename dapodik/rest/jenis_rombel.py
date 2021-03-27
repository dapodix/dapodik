import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class JenisRombel:
    jenis_rombel: int
    nm_jenis_rombel: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nm_jenis_rombel

    class Prop(BaseProp):
        @property
        def jenisrombel(self) -> "JenisRombel":
            return self.dapodik._find(
                self.dapodik.jenis_rombel(),
                lambda x: x.jenis_rombel == getattr(self, "jenis_rombel"),
            )

        @jenisrombel.setter
        def jenisrombel(self, value: "JenisRombel"):
            new = self.dapodik._find(
                self.dapodik.jenis_rombel(),
                lambda x: x.jenis_rombel == value.jenis_rombel,
            )
            setattr(self, "jenis_rombel", new.jenis_rombel)
