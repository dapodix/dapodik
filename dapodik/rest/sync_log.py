from datetime import datetime

from dapodik.base import dataclass


@dataclass(frozen=True, slots=True)
class SyncLog:
    id_instalasi: str
    begin_sync: datetime
    end_sync: datetime
    sync_media: str
    is_success: str
    selisih_waktu_server: str
    alamat_ip: str
    pengguna_id: str
    sync_log_id: str
