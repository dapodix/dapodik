from dataclasses import dataclass
from typing import Optional
from dapodik.base import BaseData


@dataclass
class RolePengguna(BaseData):
    id_role_pengguna: str
    sekolah_id: str
    lembaga_id: Optional[str]
    yayasan_id: Optional[str]
    la_id: Optional[str]
    dudi_id: Optional[str]
    kode_lemb_sert: Optional[str]
    pengguna_id: str
    peran_id: 53
    sk_penugasan: Optional[str]
    tgl_sk_penugasan: Optional[str]
    approval_peran: str
    tgl_kadaluwarsa: Optional[str]
    last_active: Optional[str]
    jenis_lembaga: str
    create_date: str
    last_update: str
    expired_date: Optional[str]
    last_sync: str
    pengguna_id_str: str
