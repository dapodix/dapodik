import attr
from dapodik import (
    DapodikObject,
    Semester,
    Ruang,
    TingkatPendidikan,
    Pembelajaran,
    Sekolah,
)
from dapodik.utils.decorator import set_meta


@set_meta(
    "jadwal_id",
    sekolah=Sekolah,
    semester=Semester,
    pembelajaran=Pembelajaran,
    tingkat_pendidikan=TingkatPendidikan,
    ruang=Ruang,
)
@attr.dataclass
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
