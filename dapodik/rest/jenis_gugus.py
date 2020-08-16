from dataclasses import dataclass
from typing import Optional
from dapodik.base import BaseData


@dataclass
class JenisGugus(BaseData):
    jenis_gugus_id: str
    jenis_gugus: str
    create_date: str
    last_update: str
    expired_date: Optional[str]
    last_sync: str
