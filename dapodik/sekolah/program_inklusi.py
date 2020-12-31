import attr
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject, Sekolah
from dapodik.utils.decorator import set_meta


@set_meta("id_pi", sekolah=Sekolah)
@attr.dataclass
class ProgramInklusi(DapodikObject):
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
