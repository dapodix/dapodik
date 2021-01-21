from datetime import datetime

from dapodik.base import dataclass, freeze


@dataclass
class BukuLongitudinal:
    id_buku: str
    semester_id: str
    jumlah: int
    status_kelaikan: str
    id_buku_str: str
    semester_id_str: str
    buku_longitudinal_id: str
    create_date: datetime = freeze(default=None)
    last_update: datetime = freeze(default=None)
    soft_delete: str = freeze(default=None)
    last_sync: datetime = freeze(default=None)
    updater_id: str = freeze(default=None)
