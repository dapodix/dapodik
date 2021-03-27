import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class Agama:
    agama_id: int
    nama: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nama

    class Prop(BaseProp):
        @property
        def agama(self) -> "Agama":
            return self.dapodik._find(
                self.dapodik.agama(), lambda x: x.agama_id == getattr(self, "agama_id")
            )

        @agama.setter
        def agama(self, value: "Agama"):
            new_agama = self.dapodik._find(
                self.dapodik.agama(), lambda x: x.agama_id == value.agama_id
            )
            setattr(self, "agama_id", new_agama.agama_id)
