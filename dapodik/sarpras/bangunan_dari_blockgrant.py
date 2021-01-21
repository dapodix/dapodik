from datetime import datetime

from dapodik.base import dataclass, freeze


@dataclass
class BangunanDariBlockgrant:
    blockgrant_id: str
    id_bangunan: str
    blockgrant_id_str: str
    id_bangunan_str: str
    bangunan_dari_blockgrant_id: str
    create_date: datetime = freeze(default=None)
    last_update: datetime = freeze(default=None)
    soft_delete: str = freeze(default=None)
    last_sync: datetime = freeze(default=None)
    updater_id: str = freeze(default=None)
