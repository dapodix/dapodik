from datetime import datetime, date
from typing import Optional
from uuid import UUID

from dapodik import __tahun_ajaran__
from dapodik.base import dataclass, freeze


@dataclass
class PesertaDidikBaru:
    pdb_id: UUID = freeze(default="Admin.model.PesertaDidikBaru-1")
    sekolah_id: UUID = freeze()
    nama_pd: str
    jenis_kelamin: str
    nik: str
    tempat_lahir: str
    tanggal_lahir: date
    nama_ibu_kandung: str
    jenis_pendaftaran_id: int = 1
    nisn: str = ""
    sudah_diproses: int = 0
    berhasil_diproses: int = 0
    tahun_ajaran_id: int = freeze(default=__tahun_ajaran__)
    tahun_ajaran_id_str: str = ""
    peserta_didik_id: UUID = freeze(default="")
    peserta_didik_id_str: UUID = freeze(default="")
    # Get only
    create_date: Optional[datetime] = freeze(default=None)
    last_update: Optional[datetime] = freeze(default=None)
    soft_delete: Optional[int] = freeze(default=None)
    last_sync: Optional[datetime] = freeze(default=None)
    updater_id: Optional[UUID] = freeze(default=None)
