from datetime import datetime
from typing import Optional

from dapodik.base import dataclass


@dataclass
class SekolahLongitudinal:
    sekolah_id: str
    semester_id: str
    waktu_penyelenggaraan_id: str
    kontinuitas_listrik: str
    jarak_listrik: int
    wilayah_terpencil: str
    wilayah_perbatasan: str
    wilayah_transmigrasi: str
    wilayah_adat_terpencil: str
    wilayah_bencana_alam: str
    wilayah_bencana_sosial: str
    partisipasi_bos: str
    sertifikasi_iso_id: int
    sumber_listrik_id: str
    daya_listrik: str
    akses_internet_id: int
    akses_internet_2_id: int
    blob_id: Optional[str]
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    waktu_penyelenggaraan_id_str: str
    sekolah_id_str: str
    sekolah_longitudinal_id: str
