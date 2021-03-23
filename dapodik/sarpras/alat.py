from datetime import datetime, date
from typing import Optional
from uuid import UUID

import attr


@attr.dataclass
class Alat:
    id_alat: UUID
    jenis_sarana_id: int
    sekolah_id: UUID
    ptk_id: Optional[UUID]
    id_ruang: UUID
    id_hapus_buku: Optional[int]
    kepemilikan_sarpras_id: int
    kd_kl: Optional[str]
    kd_satker: Optional[str]
    kd_brg: Optional[str]
    nup: Optional[str]
    kode_eselon1: Optional[str]
    nama_eselon1: Optional[str]
    kode_sub_satker: Optional[str]
    nama_sub_satker: Optional[str]
    nama: str
    spesifikasi: Optional[str]
    tgl_hapus_buku: Optional[date]
    asal_data: int
    create_date: datetime
    last_update: datetime
    soft_delete: int
    last_sync: datetime
    updater_id: UUID
    id_ruang_str: str
    jenis_sarana_id_str: str
    sekolah_id_str: str
    key_match: str
    header: str
    vld_count: int = 0
    id_hapus_buku_str: Optional[str] = None
    jumlah: Optional[int] = None
    status_kelaikan: Optional[str] = None

    def __str__(self):
        return self.nama
