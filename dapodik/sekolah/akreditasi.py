from dataclasses import dataclass
from dapodik.base import BaseData


@dataclass
class Akreditasi(BaseData):
    akred_sp_id: str
    sekolah_id: str
    akred_sp_sk: str
    akred_sp_tmt: str
    akred_sp_tst: str
    akreditasi_id: str
    la_id: str
    create_date: str
    last_update: str
    soft_delete: str
    last_sync: str
    updater_id: str
    sekolah_id_str: str
    la_id_str: str
