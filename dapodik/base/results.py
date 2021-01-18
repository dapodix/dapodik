from typing import Any, List, Optional, Union
from typing_extensions import Literal

from collections import UserList


class Results(UserList):
    def __init__(
        self,
        results: int = 0,
        id: str = "",
        start: int = None,
        limit: Union[int, Literal["unlimited"]] = None,
        rows: Optional[List[Any]] = None,
    ):
        super(Results, self).__init__()
        self.results = results
        self.id = id
        self.start = start
        self.limit = limit
        if isinstance(rows, list):
            self.data = rows
        else:
            self.data = list()

    @property
    def rows(self) -> List[Any]:
        return list(self)


Results: List = Results  # NOQA
