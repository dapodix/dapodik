from dapodik import DapodikObject
from typing import Optional, Type, TypeVar, Callable

DO = TypeVar("DO", bound=DapodikObject)


def set_meta(
    id: str, default: Optional[str] = None, **kwargs: Type[DapodikObject]
) -> Callable:
    def deco(cls: DO) -> DO:
        cls._id = id
        for key, val in kwargs.items():
            prop = property(fget=val.getter, fset=val.setter)
            setattr(cls, key, prop)
        return cls

    return deco
