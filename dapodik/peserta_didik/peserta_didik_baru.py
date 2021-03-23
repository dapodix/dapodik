from datetime import datetime, date
from typing import Optional
from uuid import UUID

import attr


@attr.dataclass
class PesertaDidikBaru:
    pdb_id: UUID
    sekolah_id: UUID
    nama_pd: str
    jenis_kelamin: str
    nik: str
    tempat_lahir: str
    tanggal_lahir: date
    nama_ibu_kandung: str
    jenis_pendaftaran_id: int
    nisn: str
    sudah_diproses: int
    berhasil_diproses: int
    tahun_ajaran_id: int
    tahun_ajaran_id_str: str
    peserta_didik_id: UUID
    peserta_didik_id_str: UUID
    # Get only
    create_date: Optional[datetime] = None
    last_update: Optional[datetime] = None
    soft_delete: Optional[int] = None
    last_sync: Optional[datetime] = None
    updater_id: Optional[UUID] = None

    @attr.dataclass
    class Create:
        sekolah_id: UUID
        tahun_ajaran_id: int
        nama_pd: str
        jenis_kelamin: str
        nisn: str
        nik: str
        tempat_lahir: str
        tanggal_lahir: datetime
        nama_ibu_kandung: str
        jenis_pendaftaran_id: int
        sudah_diproses: int = 0
        berhasil_diproses: int = 0
        peserta_didik_id: str = ""
        pdb_id: str = "Admin.model.PesertaDidikBaru-1"
        sekolah_id_str: str = ""
        tahun_ajaran_id_str: str = ""
        jenis_pendaftaran_id_str: str = ""
        peserta_didik_id_str: str = ""
