from __future__ import annotations
from dataclasses import dataclass, field, InitVar
from typing import Any, List, Iterator, Optional, Tuple, TYPE_CHECKING
from .dapodik_object import DapodikObject
if TYPE_CHECKING:
    from dapodik import Dapodik

forward_references = {
    'Any': Any,
    'Tuple': Tuple,
    'Dapodik': 'Dapodik',
}


@dataclass(eq=False)
class Results:
    id: str
    start: int
    limit: int
    results: int = 0
    rows: List[DapodikObject] = field(default_factory=list)
    _dapodik: InitVar[Dapodik] = None
    _klass: InitVar[DapodikObject] = None

    def __post_init__(self, _dapodik: Dapodik, _klass: DapodikObject) -> None:
        self._klass = _klass
        _dapodik.logger.debug(
            'Berhasil mendapatkan {} sebanyak {} dengan id {}'.format(
                _klass, self.results, self.id))

    @classmethod
    def from_data(cls, klass: DapodikObject, data: dict, dapodik: Dapodik,
                  **kwargs) -> Optional[DapodikObject]:
        id = data.get('id')
        rows: List[DapodikObject] = [
            klass.from_data(da, id=id, dapodik=dapodik)
            for da in data.pop('rows')
        ]
        data['rows'] = rows
        return cls(_dapodik=dapodik, _klass=klass, **data)

    def __iter__(self) -> Iterator[DapodikObject]:
        return iter(self.rows)

    def __len__(self) -> int:
        return self.results

    def __getitem__(self, index) -> Optional[DapodikObject]:
        if type(index) == int:
            return self.rows[index]
        for do in self.rows:
            if do.id == index:
                return do

    def __bool__(self) -> bool:
        return bool(self.rows)

    def __hash__(self) -> int:
        if self.results > 0:
            return self.get_hash(self.id)
        return super().__hash__()

    @classmethod
    def get_hash(cls, id: str) -> int:
        return hash((cls.__class__, cls.id))
