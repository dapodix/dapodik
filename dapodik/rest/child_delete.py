from dataclasses import dataclass
from datetime import datetime


@dataclass(eq=False)
class ChildDelete:
    child_delete_id: int
    jumlah: int
    nama_table: str
    _id: str = 'child_delete_id'
