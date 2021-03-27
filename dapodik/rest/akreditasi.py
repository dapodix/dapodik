import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class Akreditasi:
    akreditasi_id: int
    nama: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nama

    class Prop(BaseProp):
        @property
        def akreditasi(self) -> "Akreditasi":
            return self.dapodik._find(
                self.dapodik.akreditasi(),
                lambda x: x.akreditasi_id == getattr(self, "akreditasi_id"),
            )

        @akreditasi.setter
        def akreditasi(self, value: "Akreditasi"):
            new_akreditasi = self.dapodik._find(
                self.dapodik.akreditasi(),
                lambda x: x.akreditasi_id == value.akreditasi_id,
            )
            setattr(self, "akreditasi_id", new_akreditasi.akreditasi_id)
