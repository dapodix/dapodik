import attr
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta("bentuk_lembaga_id")
@attr.dataclass(frozen=True)
class BentukLembaga(DapodikObject):
    bentuk_lembaga_id: str
    nama: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
