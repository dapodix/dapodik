from __future__ import annotations
from dacite import from_dict, Config
from datetime import datetime
from dapodik.config import BASE_URL
from dapodik.utils import get_dataclass_fields, str_to_datetime

from typing import Any, Optional, TypeVar, Tuple, TYPE_CHECKING
if TYPE_CHECKING:
    from dapodik import Dapodik

DO = TypeVar('DO', bound='DapodikObject')


class DapodikObject:
    dapodik: Dapodik = None
    _editable: bool = False
    _id: str = ''
    _url: str = ''
    _id_attrs: Tuple[Any, ...] = ()
    _base_url: str = BASE_URL

    @property
    def id(self):
        return self.__dict__.get(self._id)

    @classmethod
    def from_data(cls: DO,
                  data: dict,
                  id: Optional[str] = None,
                  url: Optional[str] = None,
                  dapodik: Optional[Dapodik] = None,
                  **kwargs) -> DapodikObject:
        fields = [field.name for field in get_dataclass_fields(cls)]
        unsafe_data = dict()
        id = id or cls._id

        for key, value in data.items():
            if key not in fields:
                unsafe_data[key] == value

        res: cls = from_dict(
            data_class=cls,
            data=data,
            config=Config(
                type_hooks={
                    DapodikObject: lambda id: dapodik[cls][id],
                    datetime: str_to_datetime
                }))

        if id:
            cls._id = id
        if url:
            cls._url = url
        if dapodik:
            cls.dapodik = dapodik
        if kwargs:
            unsafe_data.update(kwargs)
        for key, value in unsafe_data.items():
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

    def update(self, data: dict) -> None:
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self) -> str:
        return getattr(self, 'name', self._id)

    def __hash__(self) -> int:
        if self._id_attrs:
            return hash((self.__class__, self._id_attrs))
        return super().__hash__()
