import attr
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta("child_delete_id")
@attr.dataclass(frozen=True)
class ChildDelete(DapodikObject):
    child_delete_id: int
    jumlah: int
    nama_table: str
