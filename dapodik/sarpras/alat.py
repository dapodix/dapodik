from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik.base import BaseData


@dataclass
class Alat(BaseData):
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
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    id_ruang_str: str
    jenis_sarana_id_str: str
    sekolah_id_str: str
    vld_count: int
    key_match: str
    header: str