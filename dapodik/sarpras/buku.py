from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik import (DapodikObject, Sekolah, MataPelajaranKurikulum,
                     TingkatPendidikan, Ruang, Biblio)
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

    @MataPelajaranKurikulum.prop
    def mata_pelajaran(self) -> MataPelajaranKurikulum:
        return self.mata_pelajaran_id  # type: ignore

    @Sekolah.prop
    def sekolah(self) -> Sekolah:
        return self.sekolah_id  # type: ignore

    @TingkatPendidikan.prop
    def tingkat_pendidikan(self) -> TingkatPendidikan:
        return self.tingkat_pendidikan_id  # type: ignore

    @property
    def updater(self):
        return self.updater_id

    @property
    def buku(self):
        return self

    @Ruang.prop
    def ruang(self) -> Optional[Ruang]:
        return self.id_ruang  # type: ignore

    @Biblio.prop
    def biblio(self) -> Optional[Biblio]:
        return self.id_biblio  # type: ignore

    @property
    def hapus_buku(self):
        # TODO API
        return self.id_hapus_buku
