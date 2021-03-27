import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class AksesInternet:
    akses_internet_id: int
    nama: str
    media: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nama

    class Prop(BaseProp):
        @property
        def akses_internet(self) -> "AksesInternet":
            return self.dapodik._find(
                self.dapodik.akses_internet(),
                lambda x: x.akses_internet_id == getattr(self, "akses_internet_id"),
            )

        @akses_internet.setter
        def akses_internet(self, value: "AksesInternet"):
            new_akses_internet = self.dapodik._find(
                self.dapodik.akses_internet(),
                lambda x: x.akses_internet_id == value.akses_internet_id,
            )
            setattr(self, "akses_internet_id", new_akses_internet.akses_internet_id)
