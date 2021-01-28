from attr import Attribute
from typing import Any

from . import READ


def filter_asdict(attrib: Attribute, value: Any) -> bool:
    if attrib.metadata == READ:
        return False
    return True
