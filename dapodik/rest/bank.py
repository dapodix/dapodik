import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class Bank:
    id_bank: str
    nm_bank: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nm_bank

    class Prop(BaseProp):
        @property
        def bank(self) -> "Bank":
            return self.dapodik._find(
                self.dapodik.bank(),
                lambda x: x.id_bank == getattr(self, "id_bank"),
            )

        @bank.setter
        def bank(self, value: "Bank"):
            new_bank = self.dapodik._find(
                self.dapodik.bank(),
                lambda x: x.id_bank == value.id_bank,
            )
            setattr(self, "id_bank", new_bank.id_bank)
