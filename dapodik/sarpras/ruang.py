from datetime import datetime
from typing import Optional

import attr


@attr.dataclass
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
    create_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    soft_delete: Optional[str] = None
    last_sync: Optional[datetime] = None
    updater_id: Optional[str] = None
