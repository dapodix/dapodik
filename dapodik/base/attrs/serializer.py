import attr
from datetime import datetime, date
from typing import Any
from uuid import UUID


def serializer(
    inst=None, field: attr.Attribute = None, value: Any = None, name: str = None
) -> Any:
    if isinstance(value, UUID):
        return str(value)
    elif isinstance(value, datetime):
        return datetime.strftime(value, "%Y-%m-%d %H:%M:%S")
    elif isinstance(value, date):
        return date.strftime(value, "%Y-%m-%d")
    return value
