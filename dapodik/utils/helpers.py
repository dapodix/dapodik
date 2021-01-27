from attr import Attribute
from cachetools import cachedmethod as cachem
from cachetools.keys import hashkey
from functools import partial, wraps
from operator import attrgetter
from typing import Any, List, Tuple, Type, TypeVar, Union
from .get_subtypes import _get_subtypes


def get_subtypes(cls) -> Tuple[Any, ...]:
    """
    Given a qualified generic (like List[int] or Tuple[str, bool]) as input, return
    a tuple of all the classes listed inside the square brackets.
    Thank you! https://stackoverflow.com/a/55677007
    """
    return _get_subtypes(cls)


def get_field_type(field: Attribute) -> Any:
    if getattr(field.type, "__origin__", None) is Union:
        return getattr(field.type, "__args__")
    return field.type


T = TypeVar("T")


def from_dict(t: Type[T], data: dict) -> T:
    return t(**data)  # type: ignore


def from_list(t: Type[T], datas: List[dict]) -> List[T]:
    results: List[T] = list()
    for data in datas:
        results.append(from_dict(t, data))
    return results


def cachedmethod(func):
    key = func.__name__
    return wraps(func)(cachem(attrgetter("cache"), key=partial(hashkey, key)))
