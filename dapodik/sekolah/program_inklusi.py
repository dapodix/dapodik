from dataclasses import dataclass
from typing import Union


@dataclass
class ProgramInklusi:
    id_pi: str
    sekolah_id: str
    kebutuhan_khusus_id: int
    sk_pi: str
    tgl_sk_pi: str
    tmt_pi: str
    tst_pi: Union[str | None]
    ket_pi: str
    asal_data: str
    create_date: str
    last_update: str
    soft_delete: str
    last_sync: str
    updater_id: str
    sekolah_id_str: str
    kebutuhan_khusus_id_str: str
