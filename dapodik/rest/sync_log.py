from dataclasses import dataclass
from datetime import datetime
from dapodik.base import DapodikObject


@dataclass
class SyncLog(DapodikObject):
    id_instalasi: str
    begin_sync: str
    end_sync: str
    sync_media: str
    is_success: str
    selisih_waktu_server: str
    alamat_ip: str
    pengguna_id: str
    sync_log_id: str
