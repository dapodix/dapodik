from datetime import datetime
from typing import Optional

import attr


@attr.dataclass
class Tanah:
    id_tanah: str
    jenis_prasarana_id: int
    sekolah_id: str
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
    panjang: Optional[int]
    lebar: Optional[int]
    nilai_perolehan_aset: Optional[str]
    tgl_mutasi_keluar: Optional[str]
    batas: Optional[str]
    ket_tanah: Optional[str]
    luas: str
    luas_lahan_tersedia: str
    no_sertifikat_tanah: str
    asal_data: str
    jenis_prasarana_id_str: str
    sekolah_id_str: str
    vld_count: int
    create_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    soft_delete: Optional[str] = None
    last_sync: Optional[datetime] = None
    updater_id: Optional[str] = None
