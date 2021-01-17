from typing import Optional
from . import dataclass


@dataclass
class Defaults:
    sekolah_id: Optional[str] = None
    page: int = 1
    start: int = 0
    limit: int = 25
