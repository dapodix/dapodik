from dataclasses import dataclass
from datetime import datetime
from dapodik import DapodikObject, BlockGrant
from dapodik.utils.decorator import set_meta


@set_meta('bangunan_dari_blockgrant_id')
@dataclass(eq=False)
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

    @BlockGrant.prop
    def blockgrant(self) -> BlockGrant:
        return self.blockgrant_id  # type: ignore

    @property
    def updater(self):
        return self.updater_id

    @property
    def bangunan_dari_blockgrant(self):
        return self.bangunan_dari_blockgrant_id
