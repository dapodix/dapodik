from dataclasses import dataclass
from dapodik.base import BaseData
from typing import Optional


@dataclass
class SumberListrik(BaseData):
    sumber_listrik_id: str
    nama: str
    create_date: str
    last_update: str
    expired_date: Optional[str]
    last_sync: str
