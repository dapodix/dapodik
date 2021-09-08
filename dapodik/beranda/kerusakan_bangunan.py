import attr


@attr.dataclass
class KerusakanBangunan:
    no: int
    tanah: str
    bangunan: str
    kerusakan: str
    kriteria: str
    jml_ruang: int
