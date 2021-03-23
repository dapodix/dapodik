from datetime import datetime
from typing import Optional

import attr


@attr.dataclass
class Angkutan:
    id_angkutan: str
    sekolah_id: str
    ptk_id: Optional[str]
    jenis_sarana_id: int
    id_hapus_buku: Optional[str]
    kepemilikan_sarpras_id: str
    kd_kl: Optional[str]
    kd_satker: Optional[str]
    kd_brg: Optional[str]
    nup: Optional[int]
    kode_eselon1: Optional[str]
    nama_eselon1: Optional[str]
    kode_sub_satker: Optional[str]
    nama_sub_satker: Optional[str]
    nama: str
    spesifikasi: Optional[str]
    tgl_hapus_buku: Optional[str]
    merk: Optional[str]
    no_polisi: Optional[str]
    no_bpkb: Optional[str]
    alamat: Optional[str]
    asal_data: Optional[str]
    jenis_sarana_id_str: str
    sekolah_id_str: str
    vld_count: int
    create_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    soft_delete: Optional[str] = None
    last_sync: Optional[datetime] = None
    updater_id: Optional[str] = None

    def __str__(self):
        return self.nama
