from datetime import datetime
from typing import Optional

import attr


@attr.dataclass
class RuangLongitudinal:
    id_ruang: str
    semester_id: str
    blob_id: Optional[str]
    rusak_lisplang_talang: str
    ket_lisplang_talang: str
    rusak_rangka_plafon: str
    ket_rangka_plafon: str
    rusak_tutup_plafon: str
    ket_tutup_plafon: str
    rusak_bata_dinding: str
    ket_bata_dinding: str
    rusak_plester_dinding: str
    ket_plester_dinding: str
    rusak_daun_jendela: str
    ket_daun_jendela: str
    rusak_daun_pintu: str
    ket_daun_pintu: str
    rusak_kusen: str
    ket_kusen: str
    rusak_tutup_lantai: str
    ket_penutup_lantai: str
    rusak_inst_listrik: str
    ket_inst_listrik: str
    rusak_inst_air: str
    ket_inst_air: str
    rusak_drainase: str
    ket_drainase: str
    rusak_finish_struktur: str
    ket_finish_struktur: str
    rusak_finish_plafon: str
    ket_finish_plafon: str
    rusak_finish_dinding: str
    ket_finish_dinding: str
    rusak_finish_kpj: str
    ket_finish_kpj: str
    berfungsi: str
    id_ruang_str: str
    semester_id_str: str
    ruang_longitudinal_id: str
    create_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    soft_delete: Optional[str] = None
    last_sync: Optional[datetime] = None
    updater_id: Optional[str] = None
