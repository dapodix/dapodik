from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject, BlockGrant
from dapodik.utils.decorator import set_meta


@set_meta('angkutan_dari_blockgrant_id')
@dataclass(eq=False)
class AngkutanDariBlockgrant(DapodikObject):
    blockgrant_id: str
    id_angkutan: str
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    blockgrant_id_str: str
    id_angkutan_str: str
    angkutan_dari_blockgrant_id: Optional[str]

    @BlockGrant.prop
    def blockgrant(self) -> BlockGrant:
        return self.blockgrant_id  # type: ignore

    @property
    def updater(self):
        return self.updater_id
