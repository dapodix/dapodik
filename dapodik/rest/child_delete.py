import attr
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta("child_delete_id")
@attr.s(auto_attribs=True, eq=False, frozen=True)
class ChildDelete(DapodikObject):
    child_delete_id: int
    jumlah: int
    nama_table: str
