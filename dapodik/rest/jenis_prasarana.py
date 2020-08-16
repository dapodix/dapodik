from dataclasses import dataclass
from typing import Optional
from dapodik.base import BaseData


@dataclass
class JenisPrasarana(BaseData):
    jenis_prasarana_id: int
    nama: str
    a_unit_organisasi: str
    a_tanah: str
    a_bangunan: str
    a_ruang: str
    create_date: str
    last_update: str
    expired_date: Optional[str]
    last_sync: str
