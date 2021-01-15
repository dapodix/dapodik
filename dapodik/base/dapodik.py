from requests import Session, Response
from logging import getLogger, Logger
from typing import Any, Type, TypeVar, TYPE_CHECKING

from .config import HEADERS

if TYPE_CHECKING:
    from dapodik.dapodik import Dapodik

T = TypeVar("T", bound="BaseDapodik")


class BaseDapodik(object):
    __logger: Logger = getLogger("dapodik")
    __semester_id: str = "20202"

    def __init__(
        self,
        server: str = "http://localhost:5774/",
        session: Session = Session(),
    ):
        self.__server = server
        self.__session = session
        self.__session.headers.update(HEADERS)

    def _get(
        self,
        url: str,
        params: dict = None,
        **kwargs: Any,
    ) -> Response:
        return self.__session.get(self._url(url), params=params, **kwargs)

    def _post(
        self,
        url: str,
        data: dict,
        params: dict = None,
        **kwargs: Any,
    ) -> Response:
        return self.__session.post(self._url(url), data=data, params=params, **kwargs)

    def _url(self, url: str) -> str:
        if not url.startswith(self.__server):
            return self.__server + url.lstrip("/")
        return url

    @classmethod
    def _inject(cls: Type[T], parent: Type[T]) -> T:
        kwargs = {
            "server": getattr(parent, "__server"),
            "session": getattr(parent, "__session"),
        }
        return cls(**kwargs)


class DapodikChild(BaseDapodik):
    def __init__(self, dapodik: "Dapodik"):
        self.__server = dapodik.__server
        self.__session = dapodik.__session
