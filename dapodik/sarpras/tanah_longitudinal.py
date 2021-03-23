from datetime import datetime
from typing import Optional

import attr


@attr.dataclass
class TanahLongitudinal:
    id_tanah: str
    njop: float
    tahun_ajaran_id: int
    tahun_ajaran_id_str: str = ""
    id_tanah_str: str = ""
    tanah_longitudinal_id: str = "Admin.model.TanahLongitudinal-2"
    tanah_longitudinal_id_str: str = ""
    create_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    soft_delete: Optional[str] = None
    last_sync: Optional[datetime] = None
    updater_id: Optional[str] = None
