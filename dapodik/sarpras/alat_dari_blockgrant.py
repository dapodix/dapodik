from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik.base import BaseData


@dataclass
class AlatDariBlockgrant(BaseData):
    blockgrant_id: str
    id_alat: str
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    blockgrant_id_str: str
    id_alat_str: str = ''
    alat_dari_blockgrant_id: str = 'Admin.model.AlatDariBlockgrant-1'
