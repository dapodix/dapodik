from __future__ import annotations
from dapodik.config import BASE_URL

from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from dapodik import Dapodik

DO = TypeVar("DO", bound="DapodikObject")


class DapodikObject:
    dapodik: Dapodik = None  # type: ignore
    _editable: bool = False
    _id: str = ""
    _url: str = ""
    _id_attrs: Tuple[Any, ...] = ()
    _base_url: str = BASE_URL
    _params: Dict[str, str] = {}
    _name: str = ""
    _single: bool = False

    def __post_init__(self):
        super(DapodikObject, self).__init__()

    @property
    def id(self):
        return self.__dict__.get(self._id)

    @id.setter
    def id(self, value: str) -> None:
        self._id = value

    @classmethod
    def from_data(
        cls: Type[DO],
        data: dict,
        id: Optional[str] = None,
        url: Optional[str] = None,
        dapodik: Optional[Dapodik] = None,
        **kwargs
    ) -> DO:
        if id:
            cls._id = id
        if url:
            cls._url = url
        if dapodik:
            cls.dapodik = dapodik
        if kwargs:
            data.update(kwargs)
        return cls(**data)  # type: ignore

    def to_dict(self) -> dict:
        data = dict()
        for key in self.__dict__:
            if key == "dapodik" or key.startswith("_"):
                continue
            value = self.__dict__[key]
            if value is not None:
                if hasattr(value, "to_dict"):
                    data[key] = value.to_dict()
                else:
                    data[key] = value
        return data

    @property
    def create_data(self) -> dict:
        pass

    def create(self, obj: Any[DapodikObject]):
        pass

    def update(self, data: dict = None, **kwargs) -> None:
        data = data or kwargs
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @property
    def delete_params(self) -> dict:
        return {self._id: self.id} if self.id else {}

    def delete(self) -> bool:
        if not self._editable:
            raise Exception("Data {} tidak dapat dihapus".format(repr(self)))
        filename = self.dapodik.domain + self._url + "/" + self.id
        res = self.dapodik.session.delete(filename, params=self.delete_params)
        return res.ok

    def __str__(self) -> str:
        return getattr(self, "name", self._id)

    def __hash__(self) -> int:
        if self._id_attrs:
            return hash((self.id, self._id_attrs))
        return super().__hash__()

    @property
    def params(self) -> Optional[Dict[str, Any]]:
        return None

    @classmethod
    def with_id(cls: Type[DapodikObject], name) -> Type[DapodikObject]:
        cls._id = name
        return cls

    @classmethod
    def get_params(cls, **kwargs) -> Dict[str, Any]:
        params: Dict[str, Any] = cls._params or kwargs
        if type(cls.params) == dict:
            params.update(cls.params)  # type: ignore
        return params

    @classmethod
    def getter(cls: Type[DO], obj: Type[DO], key: str = "") -> Any:
        key = key or cls._id
        id_ = getattr(obj, key)
        res = obj.dapodik[cls]
        if isinstance(res, list):
            for d in res:
                if id_ == getattr(d, key):
                    return d
        elif id_ == getattr(res, key):
            return res
        return None

    @classmethod
    def setter(cls: Type[DO], obj: Type[DO], value: Any, key: str = "") -> Any:
        key = key or cls._id
        if isinstance(value, cls):
            setattr(obj, key, value)
            return
        id_ = getattr(obj, key)
        if isinstance(id_, cls):
            res = obj.dapodik[cls]
            if isinstance(res, list):
                for d in res:
                    if id_ == getattr(d, key):
                        setattr(obj, key, d)
            elif id_ == getattr(res, key):
                setattr(obj, key, res)

    @classmethod
    def maker(
        cls: Type[DO], dapodik: Any, url: str = None, skip: bool = False
    ) -> Callable[[], Optional[Union[DO, List[DO]]]]:
        if not skip:
            if url:
                if url.startswith(dapodik.domain):
                    pass
                else:
                    url = dapodik.domain + url
            else:
                url = dapodik.domain + cls._url

            # Cache
            if cls not in dapodik.rests:
                dapodik.rests[cls] = cls.maker(dapodik, url, True)
            if cls._id not in dapodik.id_map:
                dapodik.id_map[cls._id] = cls

        def generator(*args, **kwargs) -> Optional[Union[DO, List[DO]]]:
            if cls in dapodik.cache:
                return dapodik.cache[cls]
            params = cls.get_params(**kwargs)
            res = dapodik.session.get(url, params=params)
            if res.ok:
                data: Dict[str, Any] = res.json()
                rows: Optional[Union[list, dict]] = data.get("rows")
                result: Optional[Union[DO, List[DO]]] = None
                if not rows:
                    pass
                elif cls._single:
                    if isinstance(rows, list):
                        result = cls.from_data(rows[0])
                    result = cls.from_data(rows)  # type: ignore
                elif isinstance(rows, list):
                    result = [cls.from_data(row) for row in rows]
            dapodik.cache[cls] = result
            return result

        return generator
