from typing import Any, Dict, Generic, Iterator, TypeVar, Union

from collections import UserDict
from typing_inspect import get_args


T = TypeVar("T")


class Results(Generic[T], UserDict):
    results: int
    id: str
    start: int
    limit: int
    rows: Any

    def __attrs_post_init__(self):
        self.__data__: Dict[Union[int, str], T] = dict()
        cls = get_args(self)[0]  # type: ignore
        for index, row in enumerate(self.rows):
            result = cls(**row)
            key = getattr(result, self.id, index)
            self.__data__[key] = result

    @property
    def data(self):
        return self.__data__

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, key) -> T:
        if key in self.data:
            return self.data[key]
        raise KeyError(key)

    def __setitem__(self, key, item) -> None:
        self.data[key] = item

    def __delitem__(self, key) -> None:
        del self.data[key]

    def __iter__(self) -> Iterator[T]:
        return iter(self.data)

    # Modify __contains__ to work correctly when __missing__ is present
    def __contains__(self, key) -> bool:
        return key in self.data

    # Now, add the methods in dicts but not in MutableMapping
    def __repr__(self):
        return repr(self.data)
