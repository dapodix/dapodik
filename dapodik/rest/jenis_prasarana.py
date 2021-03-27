import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class JenisPrasarana:
    jenis_prasarana_id: int
    nama: str
    a_unit_organisasi: str
    a_tanah: str
    a_bangunan: str
    a_ruang: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nama

    class Prop(BaseProp):
        @property
        def jenis_prasarana(self) -> "JenisPrasarana":
            return self.dapodik._find(
                self.dapodik.jenis_prasarana(),
                lambda x: x.jenis_prasarana_id == getattr(self, "jenis_prasarana_id"),
            )

        @jenis_prasarana.setter
        def jenis_prasarana(self, value: "JenisPrasarana"):
            new = self.dapodik._find(
                self.dapodik.jenis_prasarana(),
                lambda x: x.jenis_prasarana_id == value.jenis_prasarana_id,
            )
            setattr(self, "jenis_prasarana_id", new.jenis_prasarana_id)
