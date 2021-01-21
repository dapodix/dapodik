from datetime import datetime
from typing import Optional

from dapodik.base import dataclass, freeze


@dataclass
class Buku:
    id_buku: str
    mata_pelajaran_id: int
    id_ruang: Optional[str]
    sekolah_id: str
    id_biblio: Optional[str]
    tingkat_pendidikan_id: str
    nm_buku: str
    id_hapus_buku: Optional[str]
    tgl_hapus_buku: Optional[str]
    asal_data: str
    mata_pelajaran_id_str: str
    sekolah_id_str: str
    create_date: datetime = freeze(default=None)
    last_update: datetime = freeze(default=None)
    soft_delete: str = freeze(default=None)
    last_sync: datetime = freeze(default=None)
    updater_id: str = freeze(default=None)
