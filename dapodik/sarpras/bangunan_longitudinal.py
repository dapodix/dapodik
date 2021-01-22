from datetime import datetime

from dapodik.base import dataclass, freeze


@dataclass
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
    create_date: datetime = freeze(default=None)
    last_update: datetime = freeze(default=None)
    soft_delete: str = freeze(default=None)
    last_sync: datetime = freeze(default=None)
    updater_id: str = freeze(default=None)
