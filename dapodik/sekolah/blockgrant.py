from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik.base import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta('blockgrant_id')
@dataclass(eq=False)
class BlockGrant(DapodikObject):
    blockgrant_id: str
    sekolah_id: str
    nama: str
    tahun: str
    jenis_bantuan_id: int
    sumber_dana_id: str
    besar_bantuan: str
    dana_pendamping: str
    peruntukan_dana: Optional[str]
    asal_data: str
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    sekolah_id_str: str
    jenis_bantuan_id_str: str
    sumber_dana_id_str: str
    blockgrant_id: str
