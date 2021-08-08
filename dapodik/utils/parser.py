import cattr
from datetime import datetime, date
from typing import Union
from uuid import UUID


def str_to_datetime(
    data: Union[str, datetime], format: str = "%Y-%m-%d %H:%M:%S"
) -> datetime:
    if isinstance(data, datetime):
        return data
    elif type(data) == str:
        if "." in data:
            return datetime.strptime(data, format + ".%f")
        return datetime.strptime(data, format)
    else:
        return datetime.now()


def str_to_date(data: Union[str, date], format: str = "%Y-%m-%d") -> date:
    if isinstance(data, date):
        return data
    elif type(data) == str:
        return datetime.strptime(data, format).date()
    else:
        return datetime.now().date()


def datetime_to_str(data: datetime) -> str:
    return data.strftime("%Y-%m-%d %H:%M:%S")


def date_to_str(data: date) -> str:
    return data.strftime("%Y-%m-%d")


def register_hooks():
    # dict -> attr
    cattr.register_structure_hook(date, lambda d, t: str_to_date(d))
    cattr.register_structure_hook(datetime, lambda d, t: str_to_datetime(d))
    cattr.register_structure_hook(UUID, lambda d, t: UUID(d))
    # attr -> dict
    cattr.register_unstructure_hook(date, date_to_str)
    cattr.register_unstructure_hook(datetime, datetime_to_str)
    cattr.register_unstructure_hook(UUID, lambda d, t: str(d))
