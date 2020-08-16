from dataclasses import dataclass
from typing import Optional
from dapodik.base import BaseData


@dataclass
class JenisHapusBuku(BaseData):
    id_hapus_buku: str
    ket_hapus_buku: str
    u_prasarana: str
    u_sarana: str
    create_date: str
    last_update: str
    expired_date: Optional[str]
    last_sync: str
