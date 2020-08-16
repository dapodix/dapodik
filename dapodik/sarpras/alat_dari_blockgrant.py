from dataclasses import dataclass
from typing import Optional
from dapodik.base import BaseData


@dataclass
class AlatDariBlockgrant(BaseData):
    blockgrant_id: str
    id_alat: str
    create_date: str
    last_update: str
    soft_delete: str
    last_sync: str
    updater_id: str
    blockgrant_id_str: str
    id_alat_str: str = ''
    alat_dari_blockgrant_id: str = 'Admin.model.AlatDariBlockgrant-1'
