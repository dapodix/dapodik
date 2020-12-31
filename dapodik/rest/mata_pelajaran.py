import attr
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject, Jurusan
from dapodik.utils.decorator import set_meta


@set_meta("mata_pelajaran_id", jurusan=Jurusan)
@attr.dataclass(frozen=True)
class MataPelajaran(DapodikObject):
    mata_pelajaran_id: int
    nama: str
    pilihan_sekolah: str
    pilihan_buku: str
    pilihan_kepengawasan: str
    pilihan_evaluasi: str
    jurusan_id: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
