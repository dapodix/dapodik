from dataclasses import dataclass
from typing import Optional
from dapodik.base import BaseData


@dataclass
class Gmd(BaseData):
    id_gmd: str
    nm_gmd: str
    create_date: str
    last_update: str
    expired_date: Optional[str]
    last_sync: str
