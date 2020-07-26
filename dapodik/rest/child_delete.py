from dataclasses import dataclass


@dataclass
class ChildDelete:
    child_delete_id: int
    jumlah: int
    nama_table: str
