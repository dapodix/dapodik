import attr
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject, Sekolah, JenisPrasarana, Bangunan
from dapodik.utils.decorator import set_meta


@set_meta(
    "id_ruang", jenis_prasarana=JenisPrasarana, sekolah=Sekolah, bangunan=Bangunan
)
@attr.dataclass
class Ruang(DapodikObject):
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
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    jenis_prasarana_id_str: str
    id_bangunan_str: str
    sekolah_id_str: str
