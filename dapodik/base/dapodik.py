import re
import json
from logging import getLogger, Logger
from requests import Session, Response
from typing import Any, cast, List, Type, TypeVar, Tuple, Union
from typing_extensions import Literal

from . import Config, from_dict, from_list, Message, Results


T = TypeVar("T", bound="BaseDapodik")
U = TypeVar("U")
R = TypeVar("R")


class BaseDapodik:
    __all__: Tuple[Any, ...] = ()

    def __init__(self, config: Config):
        self._config = None
        self.config = config
        self.__logger: Logger = getLogger("dapodik")
        self.__post_init__()

    def __post_init__(self):
        pass

    def __getitem__(self, klass: Type[R]) -> List[R]:
        name = str(klass.__name__)
        if klass not in self.__all__:
            raise ValueError(f"{name} tidak ada di {self.__class__.__name__}")
        name = re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()
        return getattr(self, name)()

    @property
    def cache(self):
        return self.config.cache

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
        limit: Union[int, Literal["unlimited"]] = 50,
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
        filename = prefix + url if prefix else url
        return self.session.get(self._url(filename), params=params_, **kwargs)

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

    def _put(
        self, url: str, id: str = "", data: dict = None, prefix: str = "rest/", **kwargs
    ):
        url = url + id if url.endswith("/") else url + "/" + id
        filename = prefix + url if prefix else url
        headers = {"Referer": self.server, "Content-Type": "application/json"}
        return self.session.put(self._url(filename), data=json.dumps(data), headers=headers, **kwargs)

    def _url(self, url: str) -> str:
        if not url.startswith(self.server):
            return self.server + url.lstrip("/")
        return url

    def _fd(self, t: Type[U], data: dict) -> U:
        return from_dict(t, data)

    def _fl(self, t: Type[U], datas: List[dict] = None) -> List[U]:
        return from_list(t, datas) if datas else list()

    def _fr(self, t: Type[U], data: dict) -> List[U]:
        if "rows" in data:
            data["rows"] = self._fl(t, data["rows"])
        return cast(List[U], Results[U](**data))

    def _msg(self, data: dict) -> Message:
        return Message(**data)  # type: ignore
