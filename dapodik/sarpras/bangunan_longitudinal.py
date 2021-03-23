from datetime import datetime
from typing import Optional

import attr


@attr.dataclass
class BangunanLongitudinal:
    id_bangunan: str
    semester_id: str
    rusak_pondasi: str
    ket_pondasi: str
    rusak_sloop_kolom_balok: str
    ket_sloop_kolom_balok: str
    rusak_plester_struktur: str
    ket_plester_struktur: str
    rusak_kudakuda_atap: str
    ket_kudakuda_atap: str
    rusak_kaso_atap: str
    ket_kaso_atap: str
    rusak_reng_atap: str
    ket_reng_atap: str
    rusak_tutup_atap: str
    ket_tutup_atap: str
    nilai_saat_ini: str
    id_bangunan_str: str
    semester_id_str: str
    bangunan_longitudinal_id: str
    bangunan_longitudinal_id_str: str = ""
    create_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    soft_delete: Optional[str] = None
    last_sync: Optional[datetime] = None
    updater_id: Optional[str] = None
