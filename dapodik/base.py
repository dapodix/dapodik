import attr
import cattr
import json
import logging
from cachetools import LRUCache, cachedmethod
from cachetools.keys import hashkey
from functools import partial
from requests import Response, Session
from operator import attrgetter
from typing import (
    Any,
    Callable,
    Generic,
    List,
    MutableMapping,
    Optional,
    Type,
    TypeVar,
    Union,
    TYPE_CHECKING,
)

from dapodik.exception import DapodikResponseError, ServerTidakMerespon
from dapodik.message import DapodikMessage
from dapodik.utils.helper import clean_response, find_in, make_query
from dapodik.utils.parser import register_hooks

T = TypeVar("T")

if TYPE_CHECKING:
    from dapodik import Dapodik


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

    def _put(
        self,
        url: str,
        data: dict = None,
        json: dict = None,
        params: dict = None,
        headers: dict = None,
        **kwargs: Any,
    ) -> Response:
        return self.session.put(
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

    def _get_struct(
        self,
        filename: str,
        cl: Type[T],
        **kwargs,
    ) -> T:
        res = self._get(filename, **kwargs)
        data = json.loads(res.text)
        return cattr.structure(data, cl)

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
        if not res.ok:
            raise ServerTidakMerespon("Server tidak merespon")
        data: dict = json.loads(res.text)
        obj: Any = key(data) if callable(key) else data
        try:
            result = cattr.structure(obj, cl)
        except Exception as E:
            # TODO Improve error handling
            raise E
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
        res = self._post(url=path, json=data, **kwargs)
        if not res.ok:
            if "{ 'success' : false, 'message' : '" in res.text:
                message = DapodikMessage.from_fail(res.text)
                raise DapodikResponseError(message)
            raise ServerTidakMerespon("Server tidak merespon")
        raw_data: str = self._clean_response(res.text)
        res_data: dict = json.loads(raw_data)
        self.logger.debug(f"Response POST : {raw_data}")
        if "success" not in res_data:
            raise DapodikResponseError(f"No success message found in data `{raw_data}`")
        elif not res_data["success"]:
            if "message" in res_data:
                raise DapodikResponseError(res_data["message"])
            raise DapodikResponseError(f"Request failed with response :`{raw_data}`")
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

    def _put_rows(
        self,
        path: str,
        cl: Type[T],
        data: Optional[dict] = None,
        query: Optional[dict] = None,
        key: Callable[[Any], Any] = lambda x: x["rows"],
        **kwargs: Any,
    ) -> T:
        res = self._put(url=path, json=data, params=query, **kwargs)
        if not res.ok:
            if "{ 'success' : false, 'message' : '" in res.text:
                message = DapodikMessage.from_fail(res.text)
                raise DapodikResponseError(message)
            raise ServerTidakMerespon("Server tidak merespon")
        raw_data: str = self._clean_response(res.text)
        res_data: dict = json.loads(raw_data)
        self.logger.debug(f"Response PUT : {raw_data}")
        if "success" not in res_data:
            raise DapodikResponseError(f"No success message found in data `{raw_data}`")
        elif not res_data["success"]:
            if "message" in res_data:
                raise DapodikResponseError(res_data["message"])
            raise DapodikResponseError(f"Request failed with response :`{raw_data}`")
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

    def _put_rest(
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
        return self._put_rows(
            prefix + path.lstrip("/"), cl=cl, data=data, query=query, key=key
        )

    _clean_response = staticmethod(clean_response)
    _find = staticmethod(find_in)
    _register_hooks = staticmethod(register_hooks)
    _query = staticmethod(make_query)


BD = TypeVar("BD", bound=BaseDapodik)


class BaseProp(Generic[T]):
    filename: str
    cl: Type[T]
    d: BD

    def __call__(self) -> T:
        return self.d._get_rows(path=self.filename, cl=self.cl)


@attr.dataclass
class BasePRest(Generic[T]):
    filename: str
    cl: Type[T]
    dapodik: "Dapodik"
    key: str = ""

    def __attrs_post_init__(self) -> None:
        if not self.key:
            self.key = self.filename.lower() + "_id"

    @cachedmethod(
        attrgetter("dapodik.cache"), key=partial(hashkey, attrgetter("filename"))
    )
    def __call__(
        self,
        id: str = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[T]:
        return self.dapodik._get_rest(
            self.filename,
            List[self.cl],
            page,
            start,
            limit,
            query={self.key: id} if id else {},
        )
