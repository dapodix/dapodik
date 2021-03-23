from datetime import datetime
from typing import Optional

import attr


@attr.dataclass
class Bangunan:
    id_bangunan: str
    jenis_prasarana_id: int
    sekolah_id: str
    id_tanah: str
    ptk_id: Optional[str]
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
    jml_lantai: str
    thn_dibangun: Optional[str]
    luas_tapak_bangunan: Optional[str]
    vol_pondasi_m3: Optional[str]
    vol_sloop_kolom_balok_m3: Optional[str]
    panj_kudakuda_m: Optional[str]
    vol_kudakuda_m3: Optional[str]
    panj_kaso_m: Optional[str]
    panj_reng_m: Optional[str]
    luas_tutup_atap_m2: Optional[str]
    kd_satker_tanah: Optional[str]
    nm_satker_tanah: Optional[str]
    kd_brg_tanah: Optional[str]
    nm_brg_tanah: Optional[str]
    nup_brg_tanah: Optional[str]
    tgl_sk_pemakai: str
    tgl_hapus_buku: Optional[str]
    ket_bangunan: Optional[str]
    asal_data: str
    jenis_prasarana_id_str: str
    id_tanah_str: str
    sekolah_id_str: str
    vld_count: int
    create_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    soft_delete: Optional[str] = None
    last_sync: Optional[datetime] = None
    updater_id: Optional[str] = None
