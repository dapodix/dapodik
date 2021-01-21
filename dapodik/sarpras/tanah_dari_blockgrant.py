from datetime import datetime

from dapodik.base import dataclass, freeze


@dataclass
class TanahDariBlockgrant:
    blockgrant_id: str
    blockgrant_id_str: str
    id_tanah: str
    id_tanah_str: str = ""
    tanah_dari_blockgrant_id: str = "Admin.model.TanahDariBlockgrant-1"
    create_date: datetime = freeze(default=None)
    last_update: datetime = freeze(default=None)
    soft_delete: str = freeze(default=None)
    last_sync: datetime = freeze(default=None)
    updater_id: str = freeze(default=None)
