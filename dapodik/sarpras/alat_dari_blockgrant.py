from datetime import datetime

from dapodik.base import dataclass, freeze


@dataclass
class AlatDariBlockgrant:
    blockgrant_id: str
    id_alat: str
    blockgrant_id_str: str = ""
    id_alat_str: str = ""
    alat_dari_blockgrant_id: str = freeze(default="Admin.model.AlatDariBlockgrant-1")
    create_date: datetime = freeze(default=None)
    last_update: datetime = freeze(default=None)
    soft_delete: str = freeze(default=None)
    last_sync: datetime = freeze(default=None)
    updater_id: str = freeze(default=None)
