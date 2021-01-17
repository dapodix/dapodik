from datetime import datetime, date
from typing import Optional

from dapodik.base import dataclass, freeze


@dataclass
class Sekolah:
    sekolah_id: str = freeze()
    nama: str = freeze()
    nama_nomenklatur: Optional[str] = freeze()
    nss: str = freeze()
    npsn: str = freeze()
    bentuk_pendidikan_id: int = freeze()
    alamat_jalan: str = freeze()
    rt: Optional[str]
    rw: Optional[str]
    nama_dusun: Optional[str]
    desa_kelurahan: str = freeze()
    kode_wilayah: str = freeze()
    kode_pos: Optional[str]
    lintang: Optional[str]
    bujur: Optional[str]
    nomor_telepon: Optional[str]
    nomor_fax: Optional[str]
    email: Optional[str]
    website: Optional[str]
    kebutuhan_khusus_id: int
    status_sekolah: str = freeze()
    sk_pendirian_sekolah: str = freeze()
    tanggal_sk_pendirian: date = freeze()
    status_kepemilikan_id: str = freeze()
    yayasan_id: str
    sk_izin_operasional: str = freeze()
    tanggal_sk_izin_operasional: date = freeze()
    no_rekening: Optional[str] = freeze()
    nama_bank: Optional[str] = freeze()
    cabang_kcp_unit: Optional[str] = freeze()
    rekening_atas_nama: Optional[str] = freeze()
    mbs: str
    luas_tanah_milik: str = freeze()
    luas_tanah_bukan_milik: str = freeze()
    kode_registrasi: str = freeze()
    npwp: Optional[str] = None
    nm_wp: Optional[str] = None
    keaktifan: str = freeze()
    flag: Optional[str] = freeze()
    create_date: datetime = freeze()
    last_update: datetime = freeze()
    soft_delete: str = freeze()
    last_sync: datetime = freeze()
    updater_id: str = freeze()
    bentuk_pendidikan_id_str: str
    kode_wilayah_str: str = freeze()
    kebutuhan_khusus_id_str: str = freeze()
    yayasan_id_str: str = freeze()
    vld_count: int = freeze()
