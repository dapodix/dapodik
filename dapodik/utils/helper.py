from cachetools import cachedmethod
from cachetools.keys import hashkey
from functools import partial, wraps
from operator import attrgetter


def cached(key: str, cache_prop: str = "cache"):
    def wrapper(func):
        return wraps(func)(
            cachedmethod(attrgetter(cache_prop), key=partial(hashkey, key))(func)
        )

    return wrapper
