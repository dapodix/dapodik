import attr
from datetime import datetime
from typing import Optional

from dapodik.base import BaseProp


@attr.dataclass(frozen=True, slots=True)
class JenisHobby:
    id_hobby: int
    nm_hobby: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime

    def __str__(self):
        return self.nm_hobby

    class Prop(BaseProp):
        @property
        def jenis_hobby(self) -> "JenisHobby":
            return self.dapodik._find(
                self.dapodik.jenis_hobby(),
                lambda x: x.id_hobby == getattr(self, "id_hobby"),
            )

        @jenis_hobby.setter
        def jenis_hobby(self, value: "JenisHobby"):
            new_jenis_hobby = self.dapodik._find(
                self.dapodik.jenis_hobby(),
                lambda x: x.id_hobby == value.id_hobby,
            )
            setattr(self, "id_hobby", new_jenis_hobby.id_hobby)
