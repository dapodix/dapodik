from datetime import datetime
from typing import Optional

import attr


@attr.dataclass
class AlatLongitudinal:
    id_alat: str
    semester_id: str
    jumlah: int
    status_kelaikan: str
    id_alat_str: str
    semester_id_str: str
    alat_longitudinal_id: str
    alat_longitudinal_id_str: str = ""
    create_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    soft_delete: Optional[str] = None
    last_sync: Optional[datetime] = None
    updater_id: Optional[str] = None
