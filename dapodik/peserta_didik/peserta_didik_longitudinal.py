from dataclasses import dataclass
from dapodik.base import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta('peserta_didik_longitudinal_id')
@dataclass(eq=False)
class PesertaDidikLongitudinal(DapodikObject):
    peserta_didik_id: int
    tinggi_badan: int
    berat_badan: int
    lingkar_kepala: int = 0
    peserta_didik_longitudinal_id: int = "Admin.model.PesertaDidikLongitudinal-1"
    semester_id: int = "20201"
    jarak_rumah_ke_sekolah_km: int = 1
    jarak_rumah_ke_sekolah: int = 1
    waktu_tempuh_ke_sekolah: int = 0
    menit_tempuh_ke_sekolah: int = 1
    jumlah_saudara_kandung: int = 0
    vld_count: int = 0
    peserta_didik_longitudinal_id_str: int = ""
    peserta_didik_id_str: int = ""
    semester_id_str: int = ""
