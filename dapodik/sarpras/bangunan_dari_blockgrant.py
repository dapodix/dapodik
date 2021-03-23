from datetime import datetime
from typing import Optional

import attr


@attr.dataclass
class BangunanDariBlockgrant:
    blockgrant_id: str
    id_bangunan: str
    blockgrant_id_str: str
    id_bangunan_str: str
    bangunan_dari_blockgrant_id: str
    create_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    soft_delete: Optional[str] = None
    last_sync: Optional[datetime] = None
    updater_id: Optional[str] = None
