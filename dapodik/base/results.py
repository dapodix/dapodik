from collections import UserDict
from typing import Any, Dict, Generic, Type, TypeVar, Union

from dapodik.base import dataclass, field


T = TypeVar("T")


@dataclass
class Results(Generic[T], UserDict):
    results: int
    id: str
    start: int
    limit: int
    rows: Any
    t: Type[T] = field(default=None)

    def __attrs_post_init__(self):
        self.__data__: Dict[Union[int, str], T] = dict()
        for index, row in enumerate(self.rows):
            result = self.t(**row)
            key = getattr(result, self.id, index)
            self.__data__[key] = result

    @property
    def data(self):
        return self.__data__

    @classmethod
    def f(cls, t: Type[T], **kwargs):
        kwargs.update(t=t)
        return cls(**kwargs)
