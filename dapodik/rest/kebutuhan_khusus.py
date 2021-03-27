import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class KebutuhanKhusus:
    kebutuhan_khusus_id: int
    kebutuhan_khusus: str
    kk_a: str
    kk_b: str
    kk_c: str
    kk_c1: str
    kk_d: str
    kk_d1: str
    kk_e: str
    kk_f: str
    kk_h: str
    kk_i: str
    kk_j: str
    kk_k: str
    kk_n: str
    kk_o: str
    kk_p: str
    kk_q: str
    untuk_lembaga: str
    untuk_ptk: str
    untuk_pd: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.kebutuhan_khusus

    class Prop(BaseProp):
        @property
        def kebutuhan_khusus(self) -> "KebutuhanKhusus":
            return self.dapodik._find(
                self.dapodik.kebutuhan_khusus(),
                lambda x: x.kebutuhan_khusus_id == getattr(self, "kebutuhan_khusus_id"),
            )

        @kebutuhan_khusus.setter
        def kebutuhan_khusus(self, value: "KebutuhanKhusus"):
            new = self.dapodik._find(
                self.dapodik.kebutuhan_khusus(),
                lambda x: x.kebutuhan_khusus_id == value.kebutuhan_khusus_id,
            )
            setattr(self, "kebutuhan_khusus_id", new.kebutuhan_khusus_id)
