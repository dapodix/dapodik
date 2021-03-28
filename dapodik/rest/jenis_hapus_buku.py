import attr
from datetime import datetime
from typing import Optional


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
