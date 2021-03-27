import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class FasilitasLayanan:
    fasilitas_layanan_id: int
    nama: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nama

    class Prop(BaseProp):
        @property
        def fasilitas_layanan(self) -> "FasilitasLayanan":
            return self.dapodik._find(
                self.dapodik.fasilitas_layanan(),
                lambda x: x.fasilitas_layanan_id
                == getattr(self, "fasilitas_layanan_id"),
            )

        @fasilitas_layanan.setter
        def fasilitas_layanan(self, value: "FasilitasLayanan"):
            new_fasilitas_layanan = self.dapodik._find(
                self.dapodik.fasilitas_layanan(),
                lambda x: x.fasilitas_layanan_id == value.fasilitas_layanan_id,
            )
            setattr(
                self, "fasilitas_layanan_id", new_fasilitas_layanan.fasilitas_layanan_id
            )
