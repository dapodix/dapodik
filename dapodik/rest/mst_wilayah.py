import attr
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta("kode_wilayah")
@attr.dataclass(frozen=True)
class MstWilayah(DapodikObject):
    kode_wilayah: str
    nama: str
    id_level_wilayah: int
    mst_kode_wilayah: Optional[str]
    negara_id: str
    asal_wilayah: Optional[str]
    kode_bps: Optional[str]
    kode_dagri: Optional[str]
    kode_keu: Optional[str]
    id_prov: Optional[str]
    id_kabkota: Optional[str]
    id_kec: Optional[str]
    a_desa: str
    a_kelurahan: str
    a_35: str
    a_urban: str
    kategori_desa_id: Optional[str]
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
