from requests import Session, Response
from logging import getLogger, Logger
from typing import Any, TypeVar

from dapodik.base import dataclass
from . import from_dict, from_list
from .config import HEADERS


T = TypeVar("T", bound="BaseDapodik")


class BaseDapodik:
    _fd = staticmethod(from_dict)
    _fl = staticmethod(from_list)

    def __init__(
        self,
        server: str = "http://localhost:5774/",
        session: Session = Session(),
        semester_id: str = "20202",
    ):
        self.__logger: Logger = getLogger("dapodik")
        self.__server = server
        self.__session = session
        self.__session.headers.update(HEADERS)
        self.__semester_id = semester_id

    @property
    def server(self) -> str:
        return self.__server

    @property
    def session(self) -> Session:
        return self.__session

    @property
    def logger(self) -> Logger:
        return self.__logger

    @property
    def semester_id(self) -> str:
        return self.__semester_id

    def _get(
        self,
        url: str,
        params: dict = None,
        **kwargs: Any,
    ) -> Response:
        return self.session.get(self._url(url), params=params, **kwargs)

    def _post(
        self,
        url: str,
        data: dict,
        params: dict = None,
        **kwargs: Any,
    ) -> Response:
        return self.session.post(self._url(url), data=data, params=params, **kwargs)

    def _url(self, url: str) -> str:
        if not url.startswith(self.server):
            return self.server + url.lstrip("/")
        return url


@dataclass
class DapodikChild(BaseDapodik):
    __server: str
    __session: Session
