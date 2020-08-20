from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik.base import DapodikObject


@dataclass
class BangunanDariBlockgrant(DapodikObject):
    blockgrant_id: str
    id_bangunan: str
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    blockgrant_id_str: str
    id_bangunan_str: str
    bangunan_dari_blockgrant_id: str
