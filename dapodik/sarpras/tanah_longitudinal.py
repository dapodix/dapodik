from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject, Tanah, TahunAjaran
from dapodik.utils.decorator import set_meta


@set_meta('tanah_longitudinal_id')
@dataclass(eq=False)
class TanahLongitudinal(DapodikObject):
    id_tanah: str
    njop: int
    tahun_ajaran_id: int
    tahun_ajaran_id_str: Optional[str] = ''
    id_tanah_str: Optional[str] = ''
    tanah_longitudinal_id: Optional[str] = 'Admin.model.TanahLongitudinal-2'
    tanah_longitudinal_id_str: Optional[str] = ''
    create_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    soft_delete: Optional[str] = None
    last_sync: Optional[datetime] = None
    updater_id: Optional[str] = None

    @Tanah.prop
    def tanah(self) -> Tanah:
        return self.id_tanah  # type: ignore

    @TahunAjaran.prop
    def tahun_ajaran(self) -> TahunAjaran:
        return self.tahun_ajaran_id  # type: ignore

    @property
    def tanah_longitudinal(self):
        return self  # type: ignore

    @property
    def updater(self):
        return self.updater_id
