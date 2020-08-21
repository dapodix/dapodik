from __future__ import annotations
from dataclasses import MISSING
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
    _params: dict = {}

    def __post_init__(self):
        self.dapodik.logger.debug('Berhasil membuat {}'.format(repr(self)))

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
        fields = [field for field in get_dataclass_fields(cls)]
        safe_data = dict()
        id = id or cls._id

        for field in fields:
            key = field.name
            if key.startswith('_'):
                continue
            value = data.pop(key)

            if value:
                if hasattr(field.type, 'from_data'):
                    safe_data[key] = dapodik[field.type][value]
                elif field.type == datetime:
                    safe_data[key] = str_to_datetime(value)
                else:
                    safe_data[key] = value
            elif field.default != MISSING:
                safe_data[key] = field.default
            elif field.default_factory != MISSING:
                safe_data[key] = field.default_factory()
            else:
                safe_data[key] = None

        res = cls(**safe_data)

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

    @property
    def params(self) -> dict:
        return None

    @classmethod
    def get_params(cls) -> dict:
        params = cls._params or {}
        if type(cls.params) == dict:
            params.update(cls.params)
        return params
