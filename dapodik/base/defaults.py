from . import dataclass


@dataclass
class Defaults:
    """Defaults

    Args:
        sekolah_id (str): ID sekolah. Default ""
        page (int): Halaman data yang diambil. Default 1
        start (int): Dimulai dari. Default 0
        limit (int): Batas data yang diambil, default 25
    """
    sekolah_id: str = ""
    page: int = 1
    start: int = 0
    limit: int = 25
