from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik import (DapodikObject, WaktuPenyelenggaraan, AksesInternet,
                     Sekolah)
from dapodik.utils.decorator import set_meta


@set_meta('sekolah_longitudinal_id')
@dataclass(eq=False)
class SekolahLongitudinal(DapodikObject):
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

    @Sekolah.property
    def sekolah(self) -> Sekolah:
        return self.sekolah_id

    @WaktuPenyelenggaraan.property
    def waktu_penyelenggaraan(self) -> WaktuPenyelenggaraan:
        return self.waktu_penyelenggaraan_id

    @AksesInternet.property
    def akses_internet(self) -> AksesInternet:
        return self.akses_internet_id

    @AksesInternet.property
    def akses_internet_2(self) -> AksesInternet:
        return self.akses_internet_2_id
