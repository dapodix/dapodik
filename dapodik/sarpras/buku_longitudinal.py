from dataclasses import dataclass
from datetime import datetime
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta('buku_longitudinal_id')
@dataclass(eq=False)
class BukuLongitudinal(DapodikObject):
    id_buku: str
    semester_id: str
    jumlah: int
    status_kelaikan: str
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    id_buku_str: str
    semester_id_str: str
    buku_longitudinal_id: str
