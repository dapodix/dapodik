from datetime import datetime
from typing import Optional

import attr


@attr.dataclass(frozen=True, slots=True)
class RolePengguna:
    id_role_pengguna: str
    sekolah_id: str
    lembaga_id: Optional[str]
    yayasan_id: Optional[str]
    la_id: Optional[str]
    dudi_id: Optional[str]
    kode_lemb_sert: Optional[str]
    pengguna_id: str
    peran_id: Optional[int]
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
