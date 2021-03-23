import json
import logging
import cattr
from datetime import date, datetime
from requests import Response, Session
from typing import Any, Callable, Optional, Type, TypeVar, Union
from uuid import UUID

from dapodik.utils.parser import str_to_date, str_to_datetime

T = TypeVar("T")


class BaseDapodik(object):
    def __init__(self, base_url: str = "http://localhost:5774/"):
        self._logger = logging.getLogger("Dapodik")
        self._session = Session()
        self._base_url = base_url
        self._register_hooks()

    @property
    def logger(self) -> logging.Logger:
        return self._logger

    @property
    def session(self) -> Session:
        return self._session

    @property
    def base_url(self) -> str:
        return self._base_url

    def _url(self, path: str) -> str:
        if path.startswith(self.base_url):
            return path
        return self.base_url + path.lstrip("/")

    def _rest_url(self, name: str) -> str:
        return self._url("rest/" + name.lstrip("/"))

    def _post(
        self,
        url: str,
        data: dict = None,
        json: dict = None,
        params: dict = None,
        headers: dict = None,
        **kwargs: Any,
    ) -> Response:
        return self.session.post(
            self._url(url),
            data=data,
            json=json,
            params=params,
            headers=headers,
            **kwargs,
        )

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

    def _get_rows(
        self,
        path: str,
        cl: Type[T],
        query: Optional[dict] = None,
        key: Callable[[Any], Any] = lambda x: x["rows"],
        **kwargs: Any,
    ) -> T:
        res = self._get(
            url=path,
            params=query,
            **kwargs,
        )
        data: dict = json.loads(res.text)
        obj: Any = key(data) if callable(key) else data
        return cattr.structure(obj, cl)

    def _get_rest(
        self,
        path: str,
        cl: Type[T],
        page: int = 1,
        start: int = 9,
        limit: Union[int, str] = 50,
        query: Optional[dict] = None,
        prefix: str = "rest/",
        key: Callable[[Any], Any] = lambda x: x["rows"],
    ) -> T:
        query = query or {
            "page": page,
            "start": start,
            "limit": limit,
        }
        return self._get_rows(prefix + path.lstrip("/"), cl=cl, query=query, key=key)

    def _register_hooks(self):
        cattr.register_structure_hook(date, lambda d, t: str_to_date(d))
        cattr.register_structure_hook(datetime, lambda d, t: str_to_datetime(d))
        cattr.register_structure_hook(UUID, lambda d, t: UUID(d))
