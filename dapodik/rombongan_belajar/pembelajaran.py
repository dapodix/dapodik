import attr
from dapodik import (
    DapodikObject,
    Semester,
    PtkTerdaftar,
    MataPelajaran,
    RombonganBelajar,
)
from dapodik.utils.decorator import set_meta


@set_meta(
    "pembelajaran_id",
    rombongan_belajar=RombonganBelajar,
    mata_pelajaran=MataPelajaran,
    ptk_terdaftar=PtkTerdaftar,
    semester=Semester,
)
@attr.dataclass
class Pembelajaran(DapodikObject):
    rombongan_belajar_id: str
    status_di_kurikulum_str: str
    mata_pelajaran_id: int
    nama_mata_pelajaran: str
    sk_mengajar: str
    ptk_terdaftar_id: str
    tanggal_sk_mengajar: str
    jam_mengajar_per_minggu: int
    induk_pembelajaran_id: str = ""
    status_di_kurikulum: int = 9
    semester_id: str = "20201"
    pembelajaran_id: str = "Admin.model.PembelajaranNew-1"

    @property
    def induk_pembelajaran(self):
        # TODO API NF
        return self.induk_pembelajaran_id
