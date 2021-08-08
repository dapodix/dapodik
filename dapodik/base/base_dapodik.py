import attr
import cattr
import json
import logging
from cachetools import LRUCache
from requests import Response, Session
from typing import Any, Callable, MutableMapping, Optional, List, Type, TypeVar, Union

from dapodik.utils.helper import clean_response, find_in, make_query
from dapodik.utils.parser import register_hooks

T = TypeVar("T")


class BaseDapodik(object):
    def __init__(self, base_url: str = "http://localhost:5774/"):
        self._logger = logging.getLogger("Dapodik")
        self._session = Session()
        self._base_url = base_url
        self._register_hooks()
        self._cache: MutableMapping = LRUCache(128)

    @property
    def cache(self) -> MutableMapping:
        return self._cache

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
        result = cattr.structure(obj, cl)
        if isinstance(result, list):
            for res in result:
                if not hasattr(res, "_dapodik"):
                    break
                setattr(res, "_dapodik", self)
        elif hasattr(result, "_dapodik"):
            setattr(res, "_dapodik", self)
        return result

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
        params = {
            "page": page,
            "start": start,
            "limit": limit,
        }
        if query:
            params.update(query)
        return self._get_rows(prefix + path.lstrip("/"), cl=cl, query=params, key=key)

    def _post_rows(
        self,
        path: str,
        cl: Type[T],
        data: Optional[dict] = None,
        query: Optional[dict] = None,
        key: Callable[[Any], Any] = lambda x: x["rows"],
        **kwargs: Any,
    ) -> T:
        res = self._post(url=path, data=data, **kwargs)
        raw_data: str = self._clean_response(res.text)
        res_data: dict = json.loads(raw_data)
        obj: Any = key(res_data) if callable(key) else res_data
        result = cattr.structure(obj, cl)
        if isinstance(result, list):
            for res in result:
                if not hasattr(res, "_dapodik"):
                    break
                setattr(res, "_dapodik", self)
        elif hasattr(result, "_dapodik"):
            setattr(res, "_dapodik", self)
        return result

    def _post_rest(
        self,
        path: str,
        cl: Type[T],
        data: Any = None,
        query: dict = None,
        prefix: str = "rest/",
        key: Callable[[Any], Any] = lambda x: x["rows"],
    ):
        if data and attr.has(type(data)):
            data = cattr.unstructure(data)
        return self._post_rows(
            prefix + path.lstrip("/"), cl=cl, data=data, query=query, key=key
        )

    _clean_response = staticmethod(clean_response)
    _find = staticmethod(find_in)
    _register_hooks = staticmethod(register_hooks)
    _query = staticmethod(make_query)
