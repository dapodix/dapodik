from datetime import datetime
from typing import Optional

import attr


@attr.dataclass
class Yayasan:
    yayasan_id: str
    nama: str
    alamat_jalan: str
    rt: str
    rw: str
    nama_dusun: str
    desa_kelurahan: str
    kode_wilayah: str
    kode_pos: str
    lintang: str
    bujur: str
    nomor_telepon: Optional[str]
    nomor_fax: Optional[str]
    email: Optional[str]
    website: Optional[str]
    npyp: Optional[str]
    nama_pimpinan_yayasan: str
    no_pendirian_yayasan: str
    tanggal_pendirian_yayasan: str
    nomor_pengesahan_pn_ln: Optional[str]
    nomor_sk_bn: Optional[str]
    tanggal_sk_bn: str
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    kode_wilayah_str: str
    vld_count: int
