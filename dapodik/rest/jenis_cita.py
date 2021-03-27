import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class JenisCita:
    id_cita: int
    nm_cita: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nm_cita

    class Prop(BaseProp):
        @property
        def cita(self) -> "JenisCita":
            return self.dapodik._find(
                self.dapodik.jenis_cita(),
                lambda x: x.id_cita == getattr(self, "id_cita"),
            )

        @cita.setter
        def cita(self, value: "JenisCita"):
            new_id_cita = self.dapodik._find(
                self.dapodik.jenis_cita(),
                lambda x: x.id_cita == value.id_cita,
            )
            setattr(self, "id_cita", new_id_cita.id_cita)
