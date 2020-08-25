from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik import (DapodikObject, WaktuPenyelenggaraan, AksesInternet,
                     Sekolah, Semester, SumberListrik)
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

    @Sekolah.prop
    def sekolah(self):
        return self.sekolah_id

    @Semester.prop
    def semester(self):
        return self.semester_id

    @WaktuPenyelenggaraan.prop
    def waktu_penyelenggaraan(self):
        return self.waktu_penyelenggaraan_id

    @property
    def sertifikasi_iso(self):
        # TODO API
        return self.sertifikasi_iso_id

    @SumberListrik.prop
    def sumber_listrik(self):
        return self.sumber_listrik_id

    @AksesInternet.prop
    def akses_internet(self):
        return self.akses_internet_id

    @AksesInternet.prop
    def akses_internet_2(self):
        return self.akses_internet_2_id

    @property
    def blob(self):
        return self.blob_id

    @property
    def updater(self):
        return self.updater_id

    def sekolah_longitudinal(self):
        return self
