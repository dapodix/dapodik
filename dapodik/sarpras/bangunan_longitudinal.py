import attr
from datetime import datetime
from dapodik import DapodikObject, Semester
from dapodik.utils.decorator import set_meta


@set_meta("bangunan_longitudinal_id", semester=Semester)
@attr.dataclass
class BangunanLongitudinal(DapodikObject):
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
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    id_bangunan_str: str
    semester_id_str: str
    bangunan_longitudinal_id: str
