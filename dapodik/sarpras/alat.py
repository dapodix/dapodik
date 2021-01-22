from datetime import datetime, date
from typing import Optional
from uuid import UUID

from dapodik.base import dataclass, freeze


@dataclass
class Alat:
    id_alat: UUID
    jenis_sarana_id: int
    sekolah_id: UUID
    ptk_id: Optional[UUID] = None
    id_ruang: UUID
    id_hapus_buku: Optional[int] = None
    kepemilikan_sarpras_id: int
    kd_kl: Optional[str] = None
    kd_satker: Optional[str] = None
    kd_brg: Optional[str] = None
    nup: Optional[str] = None
    kode_eselon1: Optional[str] = None
    nama_eselon1: Optional[str] = None
    kode_sub_satker: Optional[str] = None
    nama_sub_satker: Optional[str] = None
    nama: str
    spesifikasi: Optional[str] = None
    tgl_hapus_buku: Optional[date] = None
    asal_data: int
    create_date: datetime = freeze(default=None)
    last_update: datetime = freeze(default=None)
    soft_delete: int = freeze(default=None)
    last_sync: datetime = freeze(default=None)
    updater_id: UUID = freeze(default=None)
    id_ruang_str: str
    jenis_sarana_id_str: str
    id_hapus_buku_str: Optional[str] = None
    sekolah_id_str: str
    vld_count: int
    key_match: str
    header: str
    jumlah: Optional[int] = None
    status_kelaikan: Optional[str] = None

    def __str__(self):
        return self.nama
