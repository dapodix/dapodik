import attr
from datetime import datetime, date
from typing import Any
from uuid import UUID


def serializer(
    inst=None, field: attr.Attribute = None, value: Any = None, name: str = None
) -> Any:
    if not value:
        return value
    if not name:
        name = getattr(field, "name", "")
    if isinstance(value, list):
        out = {}
        for idx, val in enumerate(value):
            val = serializer(value=val)
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
                out.update(serializer(value=val, name=key))
            else:
                out[key] = value
        return out
    elif attr.has(value):
        return attr.asdict(value, value_serializer=serializer)  # type: ignore
    elif isinstance(value, UUID):
        return str(value)
    elif isinstance(value, datetime):
        return datetime.strftime(value, "%Y-%m-%d %H:%M:%S")
    elif isinstance(value, date):
        return date.strftime(value, "%Y-%m-%d")
    return value
