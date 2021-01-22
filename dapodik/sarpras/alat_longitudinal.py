from datetime import datetime

from dapodik.base import dataclass, freeze


@dataclass
class AlatLongitudinal:
    id_alat: str
    semester_id: str
    jumlah: int
    status_kelaikan: str
    id_alat_str: str
    semester_id_str: str
    alat_longitudinal_id: str
    alat_longitudinal_id_str: str = ""
    create_date: datetime = freeze(default=None)
    last_update: datetime = freeze(default=None)
    soft_delete: str = freeze(default=None)
    last_sync: datetime = freeze(default=None)
    updater_id: str = freeze(default=None)
