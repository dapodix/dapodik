from datetime import datetime
from typing import Optional

from dapodik.base import dataclass


@dataclass
class ProgramInklusi:
    id_pi: str
    sekolah_id: str
    kebutuhan_khusus_id: int
    sk_pi: str
    tgl_sk_pi: str
    tmt_pi: str
    tst_pi: Optional[str]
    ket_pi: str
    asal_data: str
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    sekolah_id_str: str
    kebutuhan_khusus_id_str: str
