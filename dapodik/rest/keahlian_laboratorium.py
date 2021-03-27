import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class KeahlianLaboratorium:
    keahlian_laboratorium_id: int
    nama: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nama

    class Prop(BaseProp):
        @property
        def keahlian_laboratorium(self) -> "KeahlianLaboratorium":
            return self.dapodik._find(
                self.dapodik.keahlian_laboratorium(),
                lambda x: x.keahlian_laboratorium_id
                == getattr(self, "keahlian_laboratorium_id"),
            )

        @keahlian_laboratorium.setter
        def keahlian_laboratorium(self, value: "KeahlianLaboratorium"):
            new = self.dapodik._find(
                self.dapodik.keahlian_laboratorium(),
                lambda x: x.keahlian_laboratorium_id == value.keahlian_laboratorium_id,
            )
            setattr(self, "keahlian_laboratorium_id", new.keahlian_laboratorium_id)
