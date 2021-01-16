from requests import Session
from typing import Optional

from dapodik import __semester__
from . import dataclass, field

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
    "DNT": "1",
}


@dataclass
class Config:
    f"""Config

    Args:
        username (str): Email dapodik
        password (str): Password dapodik
        server (str): Url server dapodik, default: http://localhost:5774/
        semester_id (str): ID Semester, default: {__semester__}
        sekolah_id (Optional[str]): ID Sekolah, default: None
        session (Session): Sesi
    """

    username: str
    password: str
    server: str = field(default="http://localhost:5774/")
    semester_id: str = field(default=__semester__)
    sekolah_id: Optional[str] = field(default=None)
    session: Session = field(factory=Session)
