from datetime import datetime
from uuid import UUID

import attr

DEF = "Admin.model.PesertaDidikLongitudinal-1"


@attr.dataclass
class PesertaDidikLongitudinal:
    peserta_didik_id: UUID
    semester_id: str
    tinggi_badan: int
    berat_badan: int
    lingkar_kepala: int
    jarak_rumah_ke_sekolah: int
    jarak_rumah_ke_sekolah_km: int
    waktu_tempuh_ke_sekolah: int
    menit_tempuh_ke_sekolah: int
    jumlah_saudara_kandung: int
    create_date: datetime
    last_update: datetime
    soft_delete: int
    last_sync: datetime
    updater_id: UUID
    peserta_didik_longitudinal_id_str: str
    peserta_didik_id_str: str
    semester_id_str: int
    peserta_didik_longitudinal_id: str
    vld_count: int

    @property
    def waktu_tempuh(self) -> int:
        return self.waktu_tempuh_ke_sekolah * 60 + self.menit_tempuh_ke_sekolah

    def __str__(self):
        return (
            f"TB: {self.tinggi_badan}; BB: {self.berat_badan}; LK: {self.lingkar_kepala}; "
            f""
        )

    @attr.dataclass
    class Create:
        peserta_didik_longitudinal_id: str
        semester_id: str
        peserta_didik_id: UUID
        tinggi_badan: int
        berat_badan: int
        jarak_rumah_ke_sekolah_km: int
        jarak_rumah_ke_sekolah: int
        waktu_tempuh_ke_sekolah: int
        menit_tempuh_ke_sekolah: int
        jumlah_saudara_kandung: int
        lingkar_kepala: int
        vld_count: int = 0
        peserta_didik_longitudinal_id_str: str = ""
        peserta_didik_id_str: str = ""
        semester_id_str: str = ""
