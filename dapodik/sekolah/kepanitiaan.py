import attr
from datetime import datetime
from dapodik import DapodikObject, Sekolah
from dapodik.utils.decorator import set_meta


@set_meta("id_panitia", sekolah=Sekolah)
@attr.dataclass
class Kepanitiaan(DapodikObject):
    id_panitia: str
    sekolah_id: str
    id_jns_panitia: int
    nm_panitia: str
    instansi: str
    tkt_panitia: str
    sk_tugas: str
    tmt_sk_tugas: str
    tst_sk_tugas: str
    a_pasang_papan: str
    a_formulir: str
    a_silabus: str
    a_berlaku_pos: str
    a_sosialisasi_pos: str
    a_ks_edukatif: str
    create_date: datetime
    last_update: datetime
    soft_delete: str
    last_sync: datetime
    updater_id: str
    sekolah_id_str: str
    id_jns_panitia_str: str

    @property
    def jns_panitia(self):
        # TODO API
        return self.id_jns_panitia
