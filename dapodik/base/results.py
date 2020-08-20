from __future__ import annotations
from dacite import from_dict, Config
from dataclasses import dataclass, field
from typing import Any, List, Iterator, Optional, Tuple, TYPE_CHECKING
from .dapodik_object import DapodikObject
if TYPE_CHECKING:
    from dapodik import Dapodik

forward_references = {
    'Any': Any,
    'Tuple': Tuple,
    'Dapodik': 'Dapodik',
}


@dataclass
class Results:
    id: str
    start: int
    limit: int
    results: int = 0
    rows: List[DapodikObject] = field(default_factory=list)

    @classmethod
    def from_data(cls, klass: DapodikObject, data: dict, dapodik: Dapodik,
                  **kwargs) -> Optional[DapodikObject]:
        id = data.get('id') or cls.id
        return from_dict(
            data_class=klass,
            data=data,
            config=Config(type_hooks={
                DapodikObject:
                lambda x: klass.from_data(x, id=id, dapodik=dapodik)
            },
                          forward_references=forward_references))

    def __iter__(self) -> Iterator[DapodikObject]:
        return iter(self.rows)

    def __len__(self) -> int:
        return self.results

    def __getitem__(self, index) -> Optional[DapodikObject]:
        return self.rows[index]

    def __bool__(self) -> bool:
        return bool(self.rows)
