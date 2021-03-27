import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class AlatTransportasi:
    alat_transportasi_id: int
    nama: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nama

    class Prop(BaseProp):
        @property
        def alat_transportasi(self) -> "AlatTransportasi":
            return self.dapodik._find(
                self.dapodik.alat_transportasi(),
                lambda x: x.alat_transportasi_id
                == getattr(self, "alat_transportasi_id"),
            )

        @alat_transportasi.setter
        def alat_transportasi(self, value: "AlatTransportasi"):
            new_alat_transportasi = self.dapodik._find(
                self.dapodik.alat_transportasi(),
                lambda x: x.alat_transportasi_id == value.alat_transportasi_id,
            )
            setattr(
                self, "alat_transportasi_id", new_alat_transportasi.alat_transportasi_id
            )
