from datetime import datetime
from typing import Optional

from dapodik.base import dataclass, freeze


@dataclass
class AngkutanDariBlockgrant:
    blockgrant_id: str
    id_angkutan: str
    blockgrant_id_str: str
    id_angkutan_str: str
    angkutan_dari_blockgrant_id: Optional[str]
    create_date: datetime = freeze(default=None)
    last_update: datetime = freeze(default=None)
    soft_delete: str = freeze(default=None)
    last_sync: datetime = freeze(default=None)
    updater_id: str = freeze(default=None)
