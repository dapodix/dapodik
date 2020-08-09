from dataclasses import dataclass
from dapodik.base import BaseData


@dataclass
class SyncLog(BaseData):
    id_instalasi: str
    begin_sync: str
    end_sync: str
    sync_media: str
    is_success: str
    selisih_waktu_server: str
    alamat_ip: str
    pengguna_id: str
    sync_log_id: str
