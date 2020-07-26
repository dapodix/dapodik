from dataclasses import dataclass
from dapodik.base import BaseData


@dataclass
class Yayasan(BaseData):
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
    nomor_telepon: str
    nomor_fax: str
    email: str
    website: str
    npyp: str
    nama_pimpinan_yayasan: str
    no_pendirian_yayasan: str
    tanggal_pendirian_yayasan: str
    nomor_pengesahan_pn_ln: str
    nomor_sk_bn: str
    tanggal_sk_bn: str
    create_date: str
    last_update: str
    soft_delete: str
    last_sync: str
    updater_id: str
    kode_wilayah_str: str
    vld_count: 0
