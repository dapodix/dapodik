from datetime import datetime
from uuid import UUID

from dapodik.base import dataclass


@dataclass(frozen=True, slots=True)
class AnggotaRombel:
    anggota_rombel_id: UUID
    rombongan_belajar_id: UUID
    peserta_didik_id: UUID
    jenis_pendaftaran_id: int
    create_date: datetime
    last_update: datetime
    soft_delete: int
    last_sync: datetime
    updater_id: UUID
