from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik.base import DapodikObject


@dataclass
class AlatLongitudinal(DapodikObject):
    id_alat: str
    semester_id: str
    jumlah: int
    status_kelaikan: str
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    id_alat_str: str
    semester_id_str: str
    alat_longitudinal_id: str
