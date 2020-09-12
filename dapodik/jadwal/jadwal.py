from dataclasses import dataclass
from dapodik import (DapodikObject, Semester, Ruang, TingkatPendidikan,
                     Pembelajaran, Sekolah)
from dapodik.utils.decorator import set_meta


@set_meta('jadwal_id')
@dataclass(eq=False)
class Jadwal(DapodikObject):
    jadwal_id: str
    sekolah_id: str
    semester_id: str
    id_ruang: str
    hari: str
    pembelajaran_ke: str
    pembelajaran_id: str
    pembelajaran_id_str: str
    ptk_id_str: str
    jenis_rombel: str
    tingkat_pendidikan_id: str
    rombongan_belajar_id_str: str
    id_ruang_str: str
    valid: bool

    @property
    def jadwal(self):
        return self

    @Sekolah.prop
    def sekolah(self):
        return self.sekolah_id  # type: ignore

    @Semester.prop
    def semester(self):
        return self.semester_id  # type: ignore

    @Pembelajaran.prop
    def pembelajaran(self):
        return self.pembelajaran_id  # type: ignore

    @TingkatPendidikan.prop
    def tingkat_pendidikan(self):
        return self.tingkat_pendidikan_id  # type: ignore

    @Ruang.prop
    def ruang(self):
        return self.id_ruang  # type: ignore
