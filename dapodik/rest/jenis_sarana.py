import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class JenisSarana:
    jenis_sarana_id: int
    nama: str
    kelompok: Optional[str]
    perlu_penempatan: int
    keterangan: str
    a_alat: int
    a_angkutan: int
    spm_qty_min_per_siswa: str
    spm_qty_min_per_sekolah: int
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    class Prop(BaseProp):
        @property
        def jenis_sarana(self) -> "JenisSarana":
            return self.dapodik._find(
                self.dapodik.jenis_sarana(),
                lambda x: x.jenis_sarana_id == getattr(self, "jenis_sarana_id"),
            )

        @jenis_sarana.setter
        def jenis_sarana(self, value: "JenisSarana"):
            new = self.dapodik._find(
                self.dapodik.jenis_sarana(),
                lambda x: x.jenis_sarana_id == value.jenis_sarana_id,
            )
            setattr(self, "jenis_sarana_id", new.jenis_sarana_id)
