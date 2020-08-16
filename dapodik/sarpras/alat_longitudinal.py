from dataclasses import dataclass
from typing import Optional
from dapodik.base import BaseData


@dataclass
class AlatLongitudinal(BaseData):
    id_alat: str
    semester_id: str
    jumlah: int
    status_kelaikan: str
    create_date: str
    last_update: str
    soft_delete: str
    last_sync: str
    updater_id: str
    id_alat_str: str
    semester_id_str: str
    alat_longitudinal_id: str
