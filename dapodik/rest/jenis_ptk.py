import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class JenisPtk:
    jenis_ptk_id: int
    jenis_ptk: str
    guru_kelas: str
    guru_matpel: str
    guru_bk: str
    guru_inklusi: str
    guru_pengganti: str
    pengawas_satdik: str
    pengawas_plb: str
    pengawas_matpel: str
    pengawas_bidang: str
    tas: str
    tendik_lainnya: str
    formal: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.jenis_ptk

    class Prop(BaseProp):
        @property
        def jenis_ptk(self) -> "JenisPtk":
            return self.dapodik._find(
                self.dapodik.jenis_ptk(),
                lambda x: x.jenis_ptk_id == getattr(self, "jenis_ptk_id"),
            )

        @jenis_ptk.setter
        def jenis_ptk(self, value: "JenisPtk"):
            new = self.dapodik._find(
                self.dapodik.jenis_ptk(),
                lambda x: x.jenis_ptk_id == value.jenis_ptk_id,
            )
            setattr(self, "jenis_ptk_id", new.jenis_ptk_id)
