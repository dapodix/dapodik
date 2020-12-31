import attr
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta("pengguna_id")
@attr.dataclass
class Pengguna(DapodikObject):
    pengguna_id: str
    sekolah_id: str
    lembaga_id: Optional[str]
    yayasan_id: Optional[str]
    la_id: Optional[str]
    dudi_id: Optional[str]
    kode_lemb_sert: Optional[str]
    peserta_didik_id: Optional[str]
    username: str
    a_bot: str
    nama: str
    tempat_lahir: Optional[str]
    tgl_lahir: Optional[str]
    jenis_kelamin: str
    nip_nim: Optional[str]
    jabatan_lembaga: Optional[str]
    alamat: Optional[str]
    kode_wilayah: str
    no_telepon: Optional[str]
    no_hp: Optional[str]
    approval_pengguna: str
    aktif: str
    password: str
    password_lama: str
    tgl_ganti_pwd: Optional[str]
    id_sdm_pengguna: Optional[str]
    id_pd_pengguna: Optional[str]
    token_reg: Optional[str]
    jabatan: Optional[str]
    ptk_id: str
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    ptk_id_str: str
    sekolah_id_str: str
