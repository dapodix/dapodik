from dataclasses import dataclass
from datetime import datetime, date
from dapodik import DapodikObject, Sekolah, KebutuhanKhusus, Jurusan
from dapodik.utils.decorator import set_meta


@set_meta('jurusan_sp_id')
@dataclass(eq=False, frozen=True)
class JurusanSp(DapodikObject):
    jurusan_sp_id: str
    sekolah_id: str
    kebutuhan_khusus_id: int
    jurusan_id: str
    nama_jurusan_sp: str
    sk_izin: str
    tanggal_sk_izin: date
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    sekolah_id_str: str
    kebutuhan_khusus_id_str: str
    jurusan_id_str: str
    vld_count: int

    @Sekolah.prop
    def sekolah(self) -> Sekolah:
        return self.sekolah_id  # type: ignore

    @KebutuhanKhusus.prop
    def kebutuhan_khusus(self) -> Sekolah:
        return self.kebutuhan_khusus_id  # type: ignore

    @Jurusan.prop
    def jurusan(self) -> Jurusan:
        return self.jurusan_id  # type: ignore

    @property
    def updater(self):
        return self.updater_id
