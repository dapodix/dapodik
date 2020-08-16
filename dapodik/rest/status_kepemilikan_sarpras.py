from dataclasses import dataclass
from typing import Optional
from dapodik.base import BaseData


@dataclass
class StatusKepemilikanSarpras(BaseData):
    kepemilikan_sarpras_id: str
    nama: str
    create_date: str
    last_update: str
    expired_date: Optional[str]
    last_sync: str
