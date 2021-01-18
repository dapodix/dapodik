from collections import UserList
from typing import Generic, List, Optional, Union, TypeVar
from typing_extensions import Literal

T = TypeVar("T")


class Results(Generic[T], UserList):
    def __init__(
        self,
        results: int = 0,
        id: str = "",
        start: int = None,
        limit: Union[int, Literal["unlimited"]] = None,
        rows: Optional[List[T]] = None,
    ):
        self.results = results
        self.id = id
        self.start = start
        self.limit = limit
        super(Results, self).__init__(rows)

    @property
    def rows(self) -> List[T]:
        return self.data
