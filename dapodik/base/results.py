from __future__ import annotations
from collections import UserDict
from typing import Dict, Generic, Type, TypeVar, Union, TYPE_CHECKING
from .dapodik_object import DapodikObject

if TYPE_CHECKING:
    from dapodik import Dapodik

DO = TypeVar("DO", bound=DapodikObject)


class Results(Generic[DO], UserDict):
    def __init__(
        self,
        id: str,
        start: int,
        limit: int,
        data: Dict[Union[str, int], Type[DO]],
        dapodik: Dapodik,
        klass: Type[DO],
        results: int = None,
    ):
        self.id = id
        self.start = start
        self.limit = limit
        self.results = int(results) if results else len(data)
        self.data = data or dict()
        self.klass = klass
        self.dapodik = dapodik
        dapodik.logger.debug(
            "Berhasil mendapatkan {} sebanyak {} dengan id {}".format(
                klass, self.results, self.id
            )
        )

    @classmethod
    def from_data(
        cls, klass: Type[DO], data: dict, dapodik: Dapodik, **kwargs
    ) -> Results[DO]:
        id = data.get("id")
        rows: Dict[Union[str, int], DO] = {}
        for da in data.pop("rows"):
            obj = klass.from_data(da, id=id, dapodik=dapodik)
            rows[obj.id] = obj
        data["data"] = rows
        return cls(dapodik=dapodik, klass=klass, **data)

    def __len__(self) -> int:
        return self.results or len(self.data)

    def __bool__(self) -> bool:
        return bool(self.data)

    def __hash__(self) -> int:
        if self.results > 0:
            return self.get_hash(self.id)
        return super().__hash__()

    @classmethod
    def get_hash(cls, id: str) -> int:
        return hash((cls.__class__, id))
