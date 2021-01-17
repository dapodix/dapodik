from typing import Optional
from . import dataclass


@dataclass
class Defaults:
    """Defaults

    Args:
        sekolah_id (str, optional): ID Sekolah. default None
        page (int, optional): Halaman. default 1
        start (int, optional): Start. default 0
        limit (int, optional): Limit. default 25
    """

    sekolah_id: Optional[str] = None
    page: int = 1
    start: int = 0
    limit: int = 25
