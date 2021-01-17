from dapodik.base import dataclass


@dataclass(frozen=True, slots=True)
class ChildDelete:
    child_delete_id: int
    jumlah: int
    nama_table: str
