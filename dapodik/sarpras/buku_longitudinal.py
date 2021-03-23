from datetime import datetime
from typing import Optional

import attr


@attr.dataclass
class BukuLongitudinal:
    id_buku: str
    semester_id: str
    jumlah: int
    status_kelaikan: str
    id_buku_str: str
    semester_id_str: str
    buku_longitudinal_id: str
    create_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    soft_delete: Optional[str] = None
    last_sync: Optional[datetime] = None
    updater_id: Optional[str] = None
