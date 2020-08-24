from dataclasses import dataclass
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta('child_delete_id')
@dataclass(eq=False)
class ChildDelete(DapodikObject):
    child_delete_id: int
    jumlah: int
    nama_table: str
