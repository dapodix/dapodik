from datetime import datetime
from typing import Optional

import attr


@attr.dataclass
class TanahDariBlockgrant:
    blockgrant_id: str
    blockgrant_id_str: str
    id_tanah: str
    id_tanah_str: str = ""
    tanah_dari_blockgrant_id: str = "Admin.model.TanahDariBlockgrant-1"
    create_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    soft_delete: Optional[str] = None
    last_sync: Optional[datetime] = None
    updater_id: Optional[str] = None
