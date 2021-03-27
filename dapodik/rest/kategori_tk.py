import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class KategoriTk:
    kategori_tk_id: int
    nama: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nama

    class Prop(BaseProp):
        @property
        def kategori_tk(self) -> "KategoriTk":
            return self.dapodik._find(
                self.dapodik.kategori_tk(),
                lambda x: x.kategori_tk_id == getattr(self, "kategori_tk_id"),
            )

        @kategori_tk.setter
        def kategori_tk(self, value: "KategoriTk"):
            new = self.dapodik._find(
                self.dapodik.kategori_tk(),
                lambda x: x.kategori_tk_id == value.kategori_tk_id,
            )
            setattr(self, "kategori_tk_id", new.kategori_tk_id)
