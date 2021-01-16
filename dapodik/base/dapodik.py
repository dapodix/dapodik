from requests import Session, Response
from logging import getLogger, Logger
from typing import Any, Dict, TypeVar

from . import Config, from_dict, from_list


T = TypeVar("T", bound="BaseDapodik")


class BaseDapodik:
    _fd = staticmethod(from_dict)
    _fl = staticmethod(from_list)
    __config__: Dict[str, Config] = dict()

    def __init__(self, config: Config):
        self.config = config
        self._username = ""
        self.__logger: Logger = getLogger("dapodik")

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str):
        if not isinstance(value, str):
            raise ValueError("username harus berupa str")
        self._username = value

    @property
    def config(self) -> Config:
        return self.__config__[self.username]

    @config.setter
    def config(self, value: Config):
        if not isinstance(value, Config):
            raise ValueError("config harus berupa dapodik.base.Config")
        if not self.username:
            self.username = value.username
        self.__config__[self.username] = value

    @property
    def server(self) -> str:
        return self.__config__[self.username].server

    @property
    def session(self) -> Session:
        return self.__config__[self.username].session

    @property
    def logger(self) -> Logger:
        return self.__logger

    @property
    def semester_id(self) -> str:
        return self.__config__[self.username].semester_id

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
