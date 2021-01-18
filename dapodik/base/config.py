from cachetools import Cache, LRUCache
from requests import Session
from typing import Optional, Type

from dapodik import __semester__
from . import Defaults

HEADERS = {
    "DNT": "1",
    "Referer": "http://localhost:5774/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
}


class Config:
    """Config

    Args:
        username (str): Email dapodik
        password (str): Password dapodik
        server (str, optional): Url server dapodik. Default "http://localhost:5774/".
        semester_id (str, optional): ID semester. Default 20202.
        sekolah_id (Optional[str], optional): ID sekolah. Default None.
        session (Optional[Session], optional): Sesi. Default None.
    """

    def __init__(
        self,
        username: str,
        password: str,
        server: str = "http://localhost:5774/",
        semester_id: str = __semester__,
        sekolah_id: Optional[str] = None,
        session: Optional[Session] = None,
        defaults: Optional[Defaults] = None,
        cache: Type[Cache] = LRUCache(10),
    ):
        self._username = username
        self._password = password
        if isinstance(defaults, Defaults):
            self._defaults = defaults
        else:
            self._defaults = Defaults()
        self._server = server.rstrip("/") + "/"
        self._semester_id = semester_id
        self._sekolah_id = sekolah_id
        if isinstance(session, Session):
            self._session = session
        else:
            self._session = Session()
        self.session.headers.update(HEADERS)
        self._cache = cache

    @property
    def cache(self) -> Defaults:
        return self._defaults

    @property
    def defaults(self) -> Type[Cache]:
        return self._cache

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str:
        return self._password

    @property
    def server(self) -> str:
        return self._server

    @property
    def semester_id(self) -> str:
        return self._semester_id

    @property
    def sekolah_id(self) -> Optional[str]:
        return self._sekolah_id

    @sekolah_id.setter
    def sekolah_id(self, value: str):
        if not isinstance(value, str):
            raise ValueError("sekolah_id harus berupa string")
        self._sekolah_id = value
        self.defaults.sekolah_id = value

    @property
    def session(self) -> Session:
        return self._session

    @session.setter
    def session(self, value: Session):
        if not isinstance(value, Session):
            raise ValueError("session harus instance dari requests.Session")
        self._session = value
