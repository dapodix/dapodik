from dataclasses import dataclass
from dapodik.base import BaseData


@dataclass
class SekolahLongitudinal(BaseData):
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
    blob_id: str
    create_date: str
    last_update: str
    soft_delete: str
    last_sync: str
    updater_id: str
    waktu_penyelenggaraan_id_str: str
    sekolah_id_str: str
    sekolah_longitudinal_id: str
