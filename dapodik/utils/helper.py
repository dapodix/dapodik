from cachetools import cachedmethod
from cachetools.keys import hashkey
from functools import partial, wraps
from operator import attrgetter
from typing import Callable, List, TypeVar

T = TypeVar("T")


def cached(key: str, cache_prop: str = "cache"):
    def wrapper(func):
        return wraps(func)(
            cachedmethod(attrgetter(cache_prop), key=partial(hashkey, key))(func)
        )

    return wrapper


def clean_response(data: str) -> str:
    data = data.replace("'success'", '"success"')
    data = data.replace("'message' : '", '"message" : "')
    data = data.replace("', 'rows'", ':", :"rows:"')
    return data


def make_query(self, *args, **kwargs) -> dict:
    query = dict()
    for key, val in dict(kwargs).items():
        if val is not None:
            query[key] = val
    return query


def find_in(self, obj: List[T], is_this: Callable[[T], bool]) -> T:
    for o in obj:
        if is_this(o):
            return o
    raise ValueError("No obj found")
