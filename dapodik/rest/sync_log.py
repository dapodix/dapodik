import attr
from datetime import datetime
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta("sync_log_id")
@attr.dataclass(frozen=True)
class SyncLog(DapodikObject):
    id_instalasi: str
    begin_sync: datetime
    end_sync: datetime
    sync_media: str
    is_success: str
    selisih_waktu_server: str
    alamat_ip: str
    pengguna_id: str
    sync_log_id: str
