from datetime import datetime
from typing import Optional

from dapodik.base import dataclass, freeze


@dataclass
class Alat:
    id_alat: str
    jenis_sarana_id: int
    sekolah_id: str
    ptk_id: Optional[str]
    id_ruang: str
    id_hapus_buku: Optional[str]
    kepemilikan_sarpras_id: str
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
    tgl_hapus_buku: Optional[str]
    asal_data: str
    id_ruang_str: str
    jenis_sarana_id_str: str
    sekolah_id_str: str
    vld_count: int
    key_match: str
    header: str
    create_date: datetime = freeze(default=None)
    last_update: datetime = freeze(default=None)
    soft_delete: str = freeze(default=None)
    last_sync: datetime = freeze(default=None)
    updater_id: str = freeze(default=None)

    def __str__(self):
        return self.nama
