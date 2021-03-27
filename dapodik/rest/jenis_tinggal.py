import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class JenisTinggal:
    jenis_tinggal_id: int
    nama: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nama

    class Prop(BaseProp):
        @property
        def jenis_tinggal(self) -> "JenisTinggal":
            return self.dapodik._find(
                self.dapodik.jenis_tinggal(),
                lambda x: x.jenis_tinggal_id == getattr(self, "jenis_tinggal_id"),
            )

        @jenis_tinggal.setter
        def jenis_tinggal(self, value: "JenisTinggal"):
            new = self.dapodik._find(
                self.dapodik.jenis_tinggal(),
                lambda x: x.jenis_tinggal_id == value.jenis_tinggal_id,
            )
            setattr(self, "jenis_tinggal_id", new.jenis_tinggal_id)
