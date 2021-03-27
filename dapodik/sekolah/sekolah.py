from datetime import datetime, date
from typing import Optional

import attr


@attr.dataclass
class Sekolah:
    sekolah_id: str
    nama: str
    nama_nomenklatur: Optional[str]
    nss: str
    npsn: str
    bentuk_pendidikan_id: int
    alamat_jalan: str
    rt: Optional[str]
    rw: Optional[str]
    nama_dusun: Optional[str]
    desa_kelurahan: str
    kode_wilayah: str
    kode_pos: Optional[str]
    lintang: Optional[str]
    bujur: Optional[str]
    nomor_telepon: Optional[str]
    nomor_fax: Optional[str]
    email: Optional[str]
    website: Optional[str]
    kebutuhan_khusus_id: int
    status_sekolah: str
    sk_pendirian_sekolah: str
    tanggal_sk_pendirian: date
    status_kepemilikan_id: str
    yayasan_id: str
    sk_izin_operasional: str
    tanggal_sk_izin_operasional: date
    no_rekening: Optional[str]
    nama_bank: Optional[str]
    cabang_kcp_unit: Optional[str]
    rekening_atas_nama: Optional[str]
    mbs: int
    luas_tanah_milik: str
    luas_tanah_bukan_milik: str
    kode_registrasi: str
    npwp: Optional[str]
    nm_wp: Optional[str]
    keaktifan: int
    flag: Optional[str] = None
    create_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    soft_delete: Optional[str] = None
    last_sync: Optional[datetime] = None
    updater_id: Optional[str] = None
    bentuk_pendidikan_id_str: str = ""
    kode_wilayah_str: str = ""
    kebutuhan_khusus_id_str: str = ""
    yayasan_id_str: str = ""
    vld_count: int = 0
