from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject, Sekolah, SumberDanaSekolah
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

    @property
    def blockgrant(self):
        return self

    @Sekolah.property
    def sekolah(self) -> Sekolah:
        return self.sekolah_id

    @property
    def jenis_bantuan(self):
        # TODO API
        return self.jenis_bantuan_id

    @SumberDanaSekolah.property
    def sumber_dana(self) -> SumberDanaSekolah:
        return self.sumber_dana_id

    @property
    def updater(self):
        return self.updater_id
