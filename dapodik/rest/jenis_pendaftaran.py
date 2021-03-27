import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class JenisPendaftaran:
    jenis_pendaftaran_id: int
    nama: str
    daftar_sekolah: str
    daftar_rombel: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nama

    class Prop(BaseProp):
        @property
        def jenis_pendaftaran(self) -> "JenisPendaftaran":
            return self.dapodik._find(
                self.dapodik.jenis_pendaftaran(),
                lambda x: x.jenis_pendaftaran_id
                == getattr(self, "jenis_pendaftaran_id"),
            )

        @jenis_pendaftaran.setter
        def jenis_pendaftaran(self, value: "JenisPendaftaran"):
            new = self.dapodik._find(
                self.dapodik.jenis_pendaftaran(),
                lambda x: x.jenis_pendaftaran_id == value.jenis_pendaftaran_id,
            )
            setattr(self, "jenis_pendaftaran_id", new.jenis_pendaftaran_id)
