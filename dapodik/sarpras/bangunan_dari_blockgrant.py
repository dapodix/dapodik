import attr
from datetime import datetime
from dapodik import DapodikObject, BlockGrant
from dapodik.utils.decorator import set_meta


@set_meta("bangunan_dari_blockgrant_id", blockgrant=BlockGrant)
@attr.dataclass
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
