import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class JenisHapusBuku:
    id_hapus_buku: int
    ket_hapus_buku: str
    u_prasarana: str
    u_sarana: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.ket_hapus_buku

    class Prop(BaseProp):
        @property
        def jenis_hapus_buku(self) -> "JenisHapusBuku":
            return self.dapodik._find(
                self.dapodik.jenis_hapus_buku(),
                lambda x: x.id_hapus_buku == getattr(self, "id_hapus_buku"),
            )

        @jenis_hapus_buku.setter
        def jenis_hapus_buku(self, value: "JenisHapusBuku"):
            new_hapus_buku = self.dapodik._find(
                self.dapodik.jenis_hapus_buku(),
                lambda x: x.id_hapus_buku == value.id_hapus_buku,
            )
            setattr(self, "id_hapus_buku", new_hapus_buku.id_hapus_buku)
