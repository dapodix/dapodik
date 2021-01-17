from cachetools import cachedmethod as cachem
from cachetools.keys import hashkey
from functools import partial, wraps
from operator import attrgetter
from typing import List, Type, TypeVar


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
