from dataclasses import dataclass
from datetime import datetime


@dataclass
class ChildDelete:
    child_delete_id: int
    jumlah: int
    nama_table: str
