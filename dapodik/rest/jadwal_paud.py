from dataclasses import dataclass
from typing import Optional
from dapodik.base import BaseData


@dataclass
class JadwalPaud(BaseData):
    jadwal_id: str
    nama: str
    kesehatan: str
    pamts: str
    ddtk: str
    freq_parenting: str
    create_date: str
    last_update: str
    expired_date: Optional[str]
    last_sync: str
