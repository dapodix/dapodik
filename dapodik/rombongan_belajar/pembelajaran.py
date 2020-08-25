from dataclasses import dataclass
from dapodik import (DapodikObject, Semester, PtkTerdaftar,
                     MataPelajaranKurikulum, RombonganBelajar)
from dapodik.utils.decorator import set_meta


@set_meta('pembelajaran_id')
@dataclass(eq=False)
class Pembelajaran(DapodikObject):
    rombongan_belajar_id: str
    status_di_kurikulum_str: str
    mata_pelajaran_id: int
    nama_mata_pelajaran: str
    sk_mengajar: str
    ptk_terdaftar_id: str
    tanggal_sk_mengajar: str
    jam_mengajar_per_minggu: 24
    induk_pembelajaran_id: str = ""
    status_di_kurikulum: int = 9
    semester_id: str = "20201"
    pembelajaran_id: str = "Admin.model.PembelajaranNew-1"

    @RombonganBelajar.property
    def rombongan_belajar(self) -> RombonganBelajar:
        return self.rombongan_belajar_id

    @MataPelajaranKurikulum.property
    def mata_pelajaran(self) -> MataPelajaranKurikulum:
        return self.mata_pelajaran_id

    @PtkTerdaftar.property
    def ptk_terdaftar(self) -> PtkTerdaftar:
        return self.ptk_terdaftar_id

    @property
    def induk_pembelajaran(self):
        # TODO API
        return self.induk_pembelajaran_id

    @Semester.property
    def semester(self) -> Semester:
        return self.semester_id

    def pembelajaran(self):
        return self
