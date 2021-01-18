from datetime import datetime
from uuid import UUID

from dapodik import __semester__
from dapodik.base import dataclass, freeze

DEF = "Admin.model.PesertaDidikLongitudinal-1"


@dataclass
class PesertaDidikLongitudinal:
    peserta_didik_id: UUID = freeze(default=None)
    semester_id: str = freeze(default=__semester__)
    tinggi_badan: int
    berat_badan: int
    lingkar_kepala: int
    jarak_rumah_ke_sekolah: int
    jarak_rumah_ke_sekolah_km: int
    waktu_tempuh_ke_sekolah: int
    menit_tempuh_ke_sekolah: int
    jumlah_saudara_kandung: int = 0
    create_date: datetime = freeze(default=None)
    last_update: datetime = freeze(default=None)
    soft_delete: int = freeze(default=None)
    last_sync: datetime = freeze(default=None)
    updater_id: UUID = freeze(default=None)
    peserta_didik_longitudinal_id_str: str = freeze(default=None)
    peserta_didik_id_str: str = freeze(default=None)
    semester_id_str: int = freeze(default=None)
    peserta_didik_longitudinal_id: str = freeze(default=DEF)
    vld_count: int = freeze(default=None)
