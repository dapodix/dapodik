from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject, Sekolah
from dapodik.utils.decorator import set_meta


@set_meta('id_buku')
@dataclass(eq=False)
class Buku(DapodikObject):
    id_buku: str
    mata_pelajaran_id: int
    id_ruang: Optional[str]
    sekolah_id: str
    id_biblio: Optional[str]
    tingkat_pendidikan_id: str
    nm_buku: str
    id_hapus_buku: Optional[str]
    tgl_hapus_buku: Optional[str]
    asal_data: str
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    mata_pelajaran_id_str: str
    sekolah_id_str: str

    @Sekolah.property
    def sekolah(self) -> Sekolah:
        return self.sekolah_id
