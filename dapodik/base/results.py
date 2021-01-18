from collections.abc import MutableSequence
from typing import List, TypeVar, Union
from typing_extensions import Literal


T = TypeVar("T")


class Results(List[T], MutableSequence):
    def __init__(
        self,
        results: int = 0,
        id: str = "",
        start: int = None,
        limit: Union[int, Literal["unlimited"]] = None,
        rows: List[T] = None,
    ):
        super(Results, self).__init__()
        self.results = results
        self.id = id
        self.start = start
        self.limit = limit
        self.list: List[T] = list()
        if isinstance(rows, list):
            self.list.extend(rows)

    @property
    def rows(self) -> List[T]:
        return self.rows
