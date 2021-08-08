import attr
import cattr
import json
from typing import Generic, Optional, Type, TypeVar

T = TypeVar("T")


@attr.dataclass
class DapodikResult(Generic[T]):
    results: int
    id: str
    start: int
    limit: int
    rows: Optional[T] = None

    @classmethod
    def from_str(cls, data: str, cl: Type[T]):
        data_dict: dict = json.loads(data)
        if "rows" in data_dict and data_dict["rows"]:
            rows = cattr.structure(data_dict["rows"], cl)
            return cls(
                results=data_dict["results"],
                id=data_dict["id"],
                start=data_dict["start"],
                limit=data_dict["limit"],
                rows=rows,
            )
        return cls(
            results=0,
            id="",
            start=0,
            limit=0,
            rows=None,
        )
