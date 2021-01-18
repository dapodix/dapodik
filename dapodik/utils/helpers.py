from typing import Any, Tuple
from .get_subtypes import _get_subtypes


def get_subtypes(cls) -> Tuple[Any, ...]:
    """
    Given a qualified generic (like List[int] or Tuple[str, bool]) as input, return
    a tuple of all the classes listed inside the square brackets.
    Thank you! https://stackoverflow.com/a/55677007
    """
    return _get_subtypes(cls)
