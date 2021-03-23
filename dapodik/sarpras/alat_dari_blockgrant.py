from datetime import datetime
from typing import Optional

import attr


@attr.dataclass
class AlatDariBlockgrant:
    blockgrant_id: str
    id_alat: str
    blockgrant_id_str: str = ""
    id_alat_str: str = ""
    alat_dari_blockgrant_id: str = "Admin.model.AlatDariBlockgrant-1"
    create_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    soft_delete: Optional[str] = None
    last_sync: Optional[datetime] = None
    updater_id: Optional[str] = None
