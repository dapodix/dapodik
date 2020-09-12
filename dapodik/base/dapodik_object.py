from __future__ import annotations
from dataclasses import MISSING
from datetime import datetime, date
from dapodik.config import BASE_URL
from dapodik.utils.helpers import get_dataclass_fields
from dapodik.utils.parser import str_to_datetime, str_to_date

from typing import Any, Dict, Optional, Tuple, Type, TYPE_CHECKING
if TYPE_CHECKING:
    from dapodik import Dapodik


class DapodikObject(object):
    dapodik: Dapodik = None  # type: ignore
    _editable: bool = False
    _id: str = ''
    _url: str = ''
    _id_attrs: Tuple[Any, ...] = ()
    _base_url: str = BASE_URL
    _params: Dict[str, str] = {}
    _name: str = ''

    def __post_init__(self):
        super(DapodikObject, self).__init__()

    @property
    def id(self):
        return self.__dict__.get(self._id)

    @id.setter
    def id(self, value: str) -> None:
        self._id = value

    @classmethod
    def from_data(cls: Type[DapodikObject],
                  data: dict,
                  id: Optional[str] = None,
                  url: Optional[str] = None,
                  dapodik: Optional[Dapodik] = None,
                  **kwargs) -> DapodikObject:
        fields = get_dataclass_fields(cls)
        safe_data = dict()
        id = id or cls._id

        for field in fields:
            key = field.name
            if key.startswith('_'):
                continue
            value = data.pop(key)

            if value:
                if field.type == datetime:
                    safe_data[key] = str_to_datetime(value)
                elif field.type == date:
                    safe_data[key] = str_to_date(value)  # type: ignore
                else:
                    safe_data[key] = value
            elif field.default != MISSING:
                safe_data[key] = field.default
            elif field.default_factory != MISSING:  # type: ignore
                safe_data[key] = field.default_factory()  # type: ignore
            else:
                safe_data[key] = None  # type: ignore

        res = cls(**safe_data)  # type: ignore

        if id:
            cls._id = id
        if url:
            cls._url = url
        if dapodik:
            cls.dapodik = dapodik
        if kwargs:
            data.update(kwargs)
        if data:
            for key, value in data.items():
                setattr(res, key, value)
        return res

    def to_dict(self) -> dict:
        data = dict()
        for key in self.__dict__:
            if key == 'dapodik' or key.startswith('_'):
                continue
            value = self.__dict__[key]
            if value is not None:
                if hasattr(value, 'to_dict'):
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
            raise Exception('Data {} tidak dapat dihapus'.format(repr(self)))
        filename = self.dapodik.domain + self._url + '/' + self.id
        res = self.dapodik.session.delete(filename, params=self.delete_params)
        return res.ok

    def __str__(self) -> str:
        return getattr(self, 'name', self._id)

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
    def get_params(cls) -> Dict[str, Any]:
        params: Dict[str, Any] = cls._params or {}
        if type(cls.params) == dict:
            params.update(cls.params)  # type: ignore
        return params

    @classmethod
    def getter(cls: Type[DapodikObject],
               obj: Type[DapodikObject],
               key: str = '') -> Any:
        id_ = getattr(obj, key or cls._id)
        res = obj.dapodik[cls]
        return res[id_] if res else None

    @classmethod
    def setter(cls: Type[DapodikObject],
               obj: Type[DapodikObject],
               value: Any,
               key: str = '') -> Any:
        key = key or cls._id
        if isinstance(value, cls):
            setattr(obj, key, value)
        elif isinstance(getattr(obj, key), cls):
            res = obj.dapodik[cls]
            data = res[value] if res else None
            if res and data:
                setattr(obj, key, data)
