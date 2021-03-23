from datetime import datetime
from typing import Optional

import attr


@attr.dataclass
class AngkutanDariBlockgrant:
    blockgrant_id: str
    id_angkutan: str
    blockgrant_id_str: str
    id_angkutan_str: str
    angkutan_dari_blockgrant_id: Optional[str]
    create_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    soft_delete: Optional[str] = None
    last_sync: Optional[datetime] = None
    updater_id: Optional[str] = None
