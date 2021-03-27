import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class JenisKeluar:
    jenis_keluar_id: int
    ket_keluar: str
    keluar_pd: str
    keluar_ptk: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.ket_keluar

    class Prop(BaseProp):
        @property
        def jenis_keluar(self) -> Optional["JenisKeluar"]:
            try:
                return self.dapodik._find(
                    self.dapodik.jenis_keluar(),
                    lambda x: x.jenis_keluar_id == getattr(self, "jenis_keluar_id"),
                )
            except ValueError:
                return None

        @jenis_keluar.setter
        def jenis_keluar(self, value: "JenisKeluar"):
            new_jenis_keluar = self.dapodik._find(
                self.dapodik.jenis_keluar(),
                lambda x: x.jenis_keluar_id == value.jenis_keluar_id,
            )
            setattr(self, "jenis_keluar_id", new_jenis_keluar.jenis_keluar_id)
