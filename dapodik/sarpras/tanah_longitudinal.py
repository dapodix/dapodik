from datetime import datetime

from dapodik.base import dataclass, freeze


@dataclass
class TanahLongitudinal:
    id_tanah: str
    njop: float
    tahun_ajaran_id: int
    tahun_ajaran_id_str: str = ""
    id_tanah_str: str = ""
    tanah_longitudinal_id: str = "Admin.model.TanahLongitudinal-2"
    tanah_longitudinal_id_str: str = ""
    create_date: datetime = freeze(default=None)
    last_update: datetime = freeze(default=None)
    soft_delete: str = freeze(default=None)
    last_sync: datetime = freeze(default=None)
    updater_id: str = freeze(default=None)
