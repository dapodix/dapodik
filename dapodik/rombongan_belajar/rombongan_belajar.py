from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik import (DapodikObject, Sekolah, TingkatPendidikan,
                     KebutuhanKhusus, Semester, Ptk, Kurikulum, Jurusan,
                     JurusanSp)
from dapodik.utils.decorator import set_meta


@set_meta('rombongan_belajar_id')
@dataclass(eq=False)
class RombonganBelajar(DapodikObject):
    rombongan_belajar_id: str
    semester_id: str
    id_ruang: str
    sekolah_id: str
    tingkat_pendidikan_id: str
    jurusan_sp_id: Optional[str]
    kurikulum_id: int
    nama: str
    ptk_id: str
    moving_class: str
    jenis_rombel: str
    sks: str
    tanggal_mulai: str
    tanggal_selesai: str
    kebutuhan_khusus_id: int
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    semester_id_str: str
    sekolah_id_str: str
    kurikulum_id_str: str
    ptk_id_str: str
    id_ruang_str: str
    kebutuhan_khusus_id_str: str
    vld_count: int
    pembelajaran_count: int
    anggota_rombel_count: int
    jenis_rombel_str: str
    jurusan_id: str
    jurusan_id_str: str

    @property
    def rombongan_belajar(self):
        return self

    @Semester.prop
    def semester(self) -> Semester:
        return self.semester_id  # type: ignore

    @Sekolah.prop
    def sekolah(self) -> Sekolah:
        return self.sekolah_id  # type: ignore

    @TingkatPendidikan.prop
    def tingkat_pendidikan(self) -> TingkatPendidikan:
        return self.tingkat_pendidikan_id  # type: ignore

    @JurusanSp.prop
    def jurusan_sp(self):
        return self.jurusan_sp_id  # type: ignore

    @Kurikulum.prop
    def kurikulum(self) -> Kurikulum:
        return self.kurikulum_id  # type: ignore

    @Ptk.prop
    def ptk(self) -> Ptk:
        return self.ptk_id  # type: ignore

    @KebutuhanKhusus.prop
    def kebutuhan_khusus(self) -> KebutuhanKhusus:
        return self.kebutuhan_khusus_id  # type: ignore

    @property
    def updater(self):
        return self.updater_id

    @Jurusan.prop
    def jurusan(self) -> Optional[Jurusan]:
        return self.jurusan_id  # type: ignore
