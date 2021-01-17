from . import dataclass


@dataclass
class Defaults:
    sekolah_id: str = ""
    page: int = 1
    start: int = 0
    limit: int = 25
