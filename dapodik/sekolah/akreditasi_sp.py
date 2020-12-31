import attr
from datetime import datetime
from dapodik import DapodikObject, Sekolah, Akreditasi, LembagaPengangkat
from dapodik.utils.decorator import set_meta


@set_meta("akred_sp_id", akred_sp=Akreditasi, sekolah=Sekolah, la=LembagaPengangkat)
@attr.dataclass
class AkreditasiSp(DapodikObject):
    akred_sp_id: str
    sekolah_id: str
    akred_sp_sk: str
    akred_sp_tmt: str
    akred_sp_tst: str
    akreditasi_id: str
    la_id: str
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    sekolah_id_str: str
    la_id_str: str
