from dataclasses import dataclass
from typing import Optional
from dapodik.base import BaseData


@dataclass
class JenisKeluar(BaseData):
    jenis_keluar_id: str
    ket_keluar: str
    keluar_pd: str
    keluar_ptk: str
    create_date: str
    last_update: str
    expired_date: Optional[str]
    last_sync: str
