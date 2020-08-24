from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta('kategori_tk_id')
@dataclass(eq=False)
class KategoriTk(DapodikObject):
    kategori_tk_id: str
    nama: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
