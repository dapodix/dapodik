from dataclasses import dataclass
from datetime import datetime
from dapodik.base import BaseData
from typing import Optional


@dataclass
class SumberListrik(BaseData):
    sumber_listrik_id: str
    nama: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
