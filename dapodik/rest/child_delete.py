from dataclasses import dataclass
from datetime import datetime
from dapodik.utils.decorator import set_meta


@set_meta('child_delete_id')
@dataclass(eq=False)
class ChildDelete:
    child_delete_id: int
    jumlah: int
    nama_table: str
    _id: str = 'child_delete_id'
