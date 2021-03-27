import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class BentukLembaga:
    bentuk_lembaga_id: int
    nama: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nama

    class Prop(BaseProp):
        @property
        def bentuk_lembaga(self) -> "BentukLembaga":
            return self.dapodik._find(
                self.dapodik.bentuk_lembaga(),
                lambda x: x.bentuk_lembaga_id == getattr(self, "bentuk_lembaga_id"),
            )

        @bentuk_lembaga.setter
        def bentuk_lembaga(self, value: "BentukLembaga"):
            new_bentuk_lembaga_ = self.dapodik._find(
                self.dapodik.bentuk_lembaga(),
                lambda x: x.bentuk_lembaga_id == value.bentuk_lembaga_id,
            )
            setattr(self, "bentuk_lembaga_id", new_bentuk_lembaga_.bentuk_lembaga_id)
