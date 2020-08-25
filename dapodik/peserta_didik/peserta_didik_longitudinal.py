from dataclasses import dataclass
from dapodik import DapodikObject, PesertaDidik, Semester
from dapodik.utils.decorator import set_meta

DEF = "Admin.model.PesertaDidikLongitudinal-1"


@set_meta('peserta_didik_longitudinal_id')
@dataclass(eq=False)
class PesertaDidikLongitudinal(DapodikObject):
    peserta_didik_id: int
    tinggi_badan: int
    berat_badan: int
    lingkar_kepala: int = 0
    peserta_didik_longitudinal_id: int = DEF  # type: ignore
    semester_id: str = "20201"
    jarak_rumah_ke_sekolah_km: int = 1
    jarak_rumah_ke_sekolah: int = 1
    waktu_tempuh_ke_sekolah: int = 0
    menit_tempuh_ke_sekolah: int = 1
    jumlah_saudara_kandung: int = 0
    vld_count: int = 0
    peserta_didik_longitudinal_id_str: str = ""
    peserta_didik_id_str: str = ""
    semester_id_str: str = ""

    @PesertaDidik.prop
    def peserta_didik(self) -> PesertaDidik:
        return self.peserta_didik_id  # type: ignore

    @property
    def peserta_didik_longitudinal(self):
        return self

    @Semester.prop
    def semester(self) -> Semester:
        return self.semester_id  # type: ignore
