from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik.base import DapodikObject


@dataclass
class RolePengguna(DapodikObject):
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
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
    pengguna_id_str: str
