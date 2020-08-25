from dapodik import DapodikObject
from typing import Optional, Type, Callable


def set_meta(id: str, default: Optional[str] = None) -> Callable:
    def deco(cls: Type[DapodikObject]) -> Type[DapodikObject]:
        cls._id = id
        return cls

    return deco
