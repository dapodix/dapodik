from datetime import datetime, date
from typing import Optional

import attr


@attr.dataclass
class Semester:
    semester_id: str
    tahun_ajaran_id: str
    nama: str
    semester: str
    periode_aktif: str
    tanggal_mulai: date
    tanggal_selesai: date
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
