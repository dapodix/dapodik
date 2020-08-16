from dataclasses import dataclass
from typing import Optional
from dapodik.base import BaseData


@dataclass
class JenisLk(BaseData):
    id_jenis_lk: str
    nm_jenis_lk: str
    ket_jenis_lk: Optional[str]
    create_date: str
    last_update: str
    expired_date: Optional[str]
    last_sync: str
