from dataclasses import dataclass
from typing import Optional
from dapodik.base import BaseData


@dataclass
class TingkatPendidikan(BaseData):
    tingkat_pendidikan_id: str
    kode: str
    nama: str
    jenjang_pendidikan_id: str
    create_date: str
    last_update: str
    expired_date: Optional[str]
    last_sync: str
