import attr
from datetime import datetime, date
from functools import partial, wraps
from typing import Any, Callable, List, Optional

from dapodik.utils.parser import str_to_datetime, str_to_date

COMMON: List = [str, int, datetime]


def hooq(cls: type, fields: List[attr.Attribute]) -> List[attr.Attribute]:
    results: List[attr.Attribute] = list()
    return results


def frozen(_, __, ___):
    """
    Prevent an attribute to be modified.

    .. versionadded:: 20.1.0
    """
    raise attr.exceptions.FrozenAttributeError()


def serialize(
    inst=None, field: attr.Attribute = None, value: Any = None, name: str = None
) -> Any:
    if not value:
        return value
    if not name:
        name = getattr(field, "name", "")
    if isinstance(value, list):
        out = {}
        for idx, val in enumerate(value):
            val = serialize(value=val)
            if isinstance(val, dict):
                for key, value in val.items():
                    out[f"{name}[{idx}][{key}]"] = val[key]
            else:
                out_key = name or ""
                # Check if data required name prefix
                if hasattr(value, "name"):
                    out_key += f"[{getattr(value, 'name')}]"
                out_key += f"[{idx}]"
                out[out_key] = val
        return out
    elif isinstance(value, dict):
        out = {}
        for key, value in value.items():
            if isinstance(value, list):
                out.update(serialize(value=val, name=key))
            else:
                out[key] = value
        return out
    elif attr.has(value):
        return attr.asdict(value, value_serializer=serialize)  # type: ignore
    elif isinstance(value, datetime):
        return datetime.strftime(value, "%Y-%m-%d %H:%M:%S")
    elif isinstance(value, date):
        return date.strftime(value, "%Y-%m-%d")
    return value


def auto_convert(cls, fields):
    results = []
    for field in fields:
        if field.converter is not None:
            results.append(field)
            continue
        if field.type in {datetime, "datetime"}:
            converter = str_to_datetime
        elif field.type in {date, "date"}:
            converter = str_to_date
        elif field.type == Optional[field.type]:

            def converter(d=None):
                return d

        else:
            converter = None
        results.append(field.evolve(converter=converter))
    return results


asdict: Callable = wraps(attr.asdict)(
    partial(
        attr.asdict,
        value_serializer=serialize,
    )
)
dataclass: Callable = wraps(attr.attrs)(
    partial(
        attr.attrs,
        auto_attribs=True,
        field_transformer=auto_convert,
        kw_only=True,
    )
)
sdataclass: Callable = wraps(attr.attrs)(
    partial(
        attr.attrs,
        auto_attribs=True,
        field_transformer=auto_convert,
        slots=True,
        kw_only=True,
    )
)
field = attr.attrib
freeze = wraps(attr.attrib)(partial(attr.attrib, on_setattr=frozen))


def fields(converter: Callable, **kwargs):
    def conv(d: List[dict]):
        results: List = list()
        if not isinstance(d, list):
            return results
        for result in results:
            results.append(converter(**result))
        return results

    return attr.attrib(converter=conv, factory=list, **kwargs)
