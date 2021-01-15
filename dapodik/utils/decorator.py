from functools import wraps


def lazy(func):
    """Decorator that makes a property lazy-evaluated.
    Source : https://stevenloria.com/lazy-properties/
    """
    attr_name = "_lazy_" + func.__name__

    @wraps(func)
    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, func(self))
        return getattr(self, attr_name)

    return wrapper
