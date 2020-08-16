from dataclasses import dataclass
from typing import Optional
from dapodik.base import BaseData


@dataclass
class SumberAir(BaseData):
    sumber_air_id: str
    nama: str
    sumber_air: str
    sumber_minum: str
    create_date: str
    last_update: str
    expired_date: Optional[str]
    last_sync: str