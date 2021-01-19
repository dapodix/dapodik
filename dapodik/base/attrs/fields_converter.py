from attr import Attribute, NOTHING
from datetime import datetime, date
from logging import getLogger
from typing import Any, Callable, List, Optional, Union
from uuid import UUID

from dapodik.utils.parser import str_to_datetime, str_to_date


AnyCallable = Callable[[Any], Any]

loggger = getLogger(__name__)


def get_field_type(field: Attribute) -> Any:
    if getattr(field.type, "__origin__", None) is Union:
        return getattr(field.type, "__args__")
    return field.type


def make_transformer(converter: AnyCallable, field: Attribute) -> AnyCallable:
    default = field.default
    # var: str = "ABC" # "ABC"
    field_type = get_field_type(field)
    if default is NOTHING:
        allow_default = False
        # var: str # False
    elif field_type and isinstance(default, field_type):
        # var: str = "" # True
        allow_default = True
    else:
        allow_default = False
        # var: str = None # False
    is_optional = field.type == Optional[field.type]
    # TODO : Diskusikan [var: Optional[str] = None # True | var: str = None # False?]
    # Thank you. https://stackoverflow.com/a/62641842

    def transformer(val: Any) -> Any:
        if field_type and isinstance(val, field_type):
            return val
        elif val is None and is_optional:
            return None
        try:
            return converter(val)
        except TypeError:
            pass
        if allow_default:
            return default
        return val

    return transformer


def fields_converter(cls, fields: List[Attribute]):
    results: List[Attribute] = []
    for field in fields:
        if field.converter is not None:
            results.append(field)
            continue
        if field.type in {str, "str"}:
            converter = make_transformer(str, field)
        elif field.type in {int, Optional[int], "int", "Optional[int]"}:
            converter = make_transformer(int, field)
        elif field.type in {UUID, Optional[UUID], "UUID", "Optional[UUID]"}:
            converter = make_transformer(UUID, field)
        elif field.type in {
            datetime,
            Optional[datetime],
            "datetime",
            "Optional[datetime]",
        }:
            converter = make_transformer(str_to_datetime, field)
        elif field.type in {date, Optional[date], "date", "Optional[date]"}:
            converter = make_transformer(str_to_date, field)
        elif field.type == Optional[field.type]:

            def converter(d=None):
                return d

        else:
            converter = field.converter  # type: ignore
        results.append(field.evolve(converter=converter))  # type: ignore
    return results
