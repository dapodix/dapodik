from dapodik.base import dataclass


@dataclass
class Validasi:
    validasi_id: int
    table: str
    tipe: int
    keterangan: str

    def __str__(self) -> str:
        return self.keterangan
