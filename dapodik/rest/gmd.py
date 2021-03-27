import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class Gmd:
    id_gmd: str
    nm_gmd: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nm_gmd

    class Prop(BaseProp):
        @property
        def gmd(self) -> "Gmd":
            return self.dapodik._find(
                self.dapodik.gmd(),
                lambda x: x.id_gmd == getattr(self, "id_gmd"),
            )

        @gmd.setter
        def gmd(self, value: "Gmd"):
            new_id_gmd = self.dapodik._find(
                self.dapodik.gmd(),
                lambda x: x.id_gmd == value.id_gmd,
            )
            setattr(self, "id_gmd", new_id_gmd.id_gmd)
