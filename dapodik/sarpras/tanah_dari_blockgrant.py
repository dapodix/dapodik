import attr
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject, BlockGrant, Tanah
from dapodik.utils.decorator import set_meta


@set_meta("tanah_dari_blockgrant_id", blockgrant=BlockGrant, tanah=Tanah)
@attr.dataclass
class TanahDariBlockgrant(DapodikObject):
    blockgrant_id: str
    blockgrant_id_str: str
    id_tanah: str
    id_tanah_str: str = ""
    create_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    soft_delete: Optional[str] = None
    last_sync: Optional[datetime] = None
    updater_id: Optional[str] = None
    tanah_dari_blockgrant_id: str = "Admin.model.TanahDariBlockgrant-1"
