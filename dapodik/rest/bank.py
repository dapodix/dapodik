from dataclasses import dataclass
from typing import Optional
from dapodik.base import BaseData


@dataclass
class Bank(BaseData):
    id_bank: str
    nm_bank: str
    create_date: str
    last_update: str
    expired_date: Optional[str]
    last_sync: str
