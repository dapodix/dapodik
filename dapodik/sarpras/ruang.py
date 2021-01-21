from datetime import datetime
from typing import Optional

from dapodik.base import dataclass, freeze


@dataclass
class Ruang:
    id_ruang: str
    jenis_prasarana_id: int
    sekolah_id: str
    id_bangunan: str
    kd_ruang: str
    nm_ruang: str
    lantai: str
    panjang: Optional[float]
    lebar: Optional[float]
    reg_pras: Optional[str]
    kapasitas: Optional[str]
    luas_ruang: Optional[float]
    luas_plester_m2: Optional[str]
    luas_plafon_m2: Optional[str]
    luas_dinding_m2: Optional[str]
    luas_daun_jendela_m2: Optional[str]
    luas_daun_pintu_m2: Optional[str]
    panj_kusen_m: Optional[str]
    luas_tutup_lantai_m2: Optional[str]
    panj_inst_listrik_m: Optional[str]
    jml_inst_listrik: Optional[str]
    panj_inst_air_m: Optional[str]
    jml_inst_air: Optional[str]
    panj_drainase_m: Optional[str]
    luas_finish_struktur_m2: Optional[str]
    luas_finish_plafon_m2: Optional[str]
    luas_finish_dinding_m2: Optional[str]
    luas_finish_kpj_m2: Optional[str]
    jenis_prasarana_id_str: str
    id_bangunan_str: str
    sekolah_id_str: str
    create_date: datetime = freeze(default=None)
    last_update: datetime = freeze(default=None)
    soft_delete: str = freeze(default=None)
    last_sync: datetime = freeze(default=None)
    updater_id: str = freeze(default=None)
