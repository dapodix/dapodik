from requests import Session, Response
from logging import getLogger, Logger
from typing import Any, List, Type, TypeVar

from . import Config, from_dict, from_list


T = TypeVar("T", bound="BaseDapodik")
U = TypeVar("U")


class BaseDapodik:
    def __init__(self, config: Config):
        self._config = None
        self.config = config
        self.__logger: Logger = getLogger("dapodik")
        self.__post_init__()

    def __post_init__(self):
        pass

    @property
    def config(self) -> Config:
        return self._config  # type: ignore

    @config.setter
    def config(self, value: Config):
        if not isinstance(value, Config):
            raise ValueError("config harus berupa dapodik.base.Config")
        self._config = value

    @property
    def username(self) -> str:
        return self.config.username

    @property
    def server(self) -> str:
        return self.config.server

    @property
    def session(self) -> Session:
        return self.config.session

    @property
    def logger(self) -> Logger:
        return self.__logger

    @property
    def semester_id(self) -> str:
        return self.config.semester_id

    def _get(
        self,
        url: str,
        params: dict = None,
        **kwargs: Any,
    ) -> Response:
        return self.session.get(
            self._url(url),
            params=params,
            **kwargs,
        )

    def _get_rest(
        self,
        url: str,
        params: dict = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
        prefix: str = "rest/",
        **kwargs: Any,
    ) -> Response:
        params_ = {
            "page": page,
            "start": start,
            "limit": limit,
        }
        if params:
            params_.update(params)
        return self.session.get(self._url(prefix + url), params=params_, **kwargs)

    def _post(
        self,
        url: str,
        data: dict = None,
        json: dict = None,
        params: dict = None,
        **kwargs: Any,
    ) -> Response:
        return self.session.post(
            self._url(url),
            data=data,
            json=json,
            params=params,
            **kwargs,
        )

    def _url(self, url: str) -> str:
        if not url.startswith(self.server):
            return self.server + url.lstrip("/")
        return url

    def _fd(self, t: Type[U], data: dict) -> U:
        return from_dict(t, data)

    def _fl(self, t: Type[U], datas: List[dict] = None) -> List[U]:
        return from_list(t, datas) if datas else list()
