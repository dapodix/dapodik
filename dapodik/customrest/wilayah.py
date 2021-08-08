import attr
from datetime import datetime
from typing import Optional


@attr.dataclass(frozen=True, slots=True)
class Wilayah:
    kode_wilayah: str
    nama: str
    id_level_wilayah: int
    mst_kode_wilayah: str
    negara_id: str
    asal_wilayah: str
    kode_bps: str
    kode_dagri: str
    kode_keu: str
    id_prov: Optional[int]
    id_kabkota: Optional[int]
    id_kec: Optional[int]
    a_desa: int
    a_kelurahan: int
    a_35: int
    a_urban: int
    kategori_desa_id: Optional[int]
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
    nama_kabupaten: str
